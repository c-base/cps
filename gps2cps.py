#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GPS to CPS converter

Usage:
  gps2cps.py [--c=<version>] <latitude> <longitude>
  gps2cps.py (-h | --help)
  gps2cps.py --version

Options:
  -h --help      Show this screen.
  --version      Show version.
  --c=<version>  Set CPS version [default: 3].
"""

from math import radians, cos, sin, asin, acos, sqrt, degrees

from docopt import docopt

ANTENNA = (52.5207511, 13.4103148)


def haversine(latitude1, longitude1, latitude2, longitude2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    long1, lat1, long2, lat2 = map(radians, [longitude1, latitude1,
                                             longitude2, latitude2])
    # haversine formula
    dlong = long2 - long1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlong / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6371 * c

    return km * 1000


def convert3(latitude, longitude):
    distance_antenna = haversine(ANTENNA[0], ANTENNA[1], latitude, longitude)
    distance_zero = haversine(ANTENNA[0], longitude, latitude, longitude)
    angle = degrees(acos(distance_zero / distance_antenna)) - 7.675214

    if distance_antenna > 825:
        print('Warning! Position is outside of c-base spacestation. Remember to were your space suit!')
    return 'c3c%.2fc%.2fc0' % (angle, distance_antenna)


if __name__ == '__main__':
    args = docopt(__doc__, version='0.1.0')

    latitude = float(args['<latitude>'])
    longitude = float(args['<longitude>'])

    if args['--c'] == '3':
        coords = convert3(latitude, longitude)
        print('GPS coords: %f, %f\nCPS coords: %s' % (latitude, longitude, coords))
    else:
        print('Sorry this CPS version isn\'t implemented yet.')
