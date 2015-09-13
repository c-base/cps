CPS
===

The CPS is for positioning artefacts on board the station, and not using GPS, as an global positioning system is unusable in context of liftoff from earth. 
It is a cylyndrical positioning system.

![image](http://mathworld.wolfram.com/images/eps-gif/CylindricalCoordinates_1001.gif)

## directions

### corewards

core is the true core and the only point where you can't go corewards.
core is defined as `c0c0c0c0` or the REal core __`c0Re`__ and the main-antenna marks its position.

### clampwards

when you're going towards the rim of the spacectation.

### clockwise

going ___against___ how you would write the letter ___`C`___

### counterclockwise

going ___with___  the way one would write the letter ___`C`___.

### level

We have excavated 3 levels

Level  1 -  c_huttle & tower  
Level  cero - mainhall  
Level -1 - nerdarea and labs  

## notation

### short format

Bold uppercase c in code style ___`C`___

### long format

c is a good separator and will be used to separate all parts of the coordinates.

```
c{version, 3}c{(circular) angle}c{distance from core, radial distance r}c{level}
```

```
c\d+c{0.0-360.0}c\d+c(-)\d+
```

Example: `c3c30c1140c0` (mainhall)

#### The first element: version number

Right now we are in the 3rd reconstructions phase and therefore should use version `c3` but still only have and use `c2` maps. If we refer to location on the previous configurations, we change the version number accordingly.
There is a transformation matrix for transforming coordinates between versions.

#### The second element: the angle

Is a float number. c-base is at `c30`
