# Degassing Boundary Condition for OpenFOAM Using fvOptions

## Overview

This is a sample `fvOptions` file that can be used to implement a degassing boundary condition for multiphase flows where the free surface is not modelled directly. At all cells adjacent to the degassing boundaries, a mass source is applied to remove the mass of gas within one timestep. To account for the mass sink, a force is also added to the momentum equations to balance the force due to the removal of mass. 

## How to Use

The continous liquid phase should be set up as a `slip` wall on the degassing boundary, while the dispersed phase should be set up as a `pressureInletOutletVelocity` boundary. The pressure field, `p_rgh` should be set as `prghPressure` condition on the degassing boundary. This code has mainly been tested with the `reactingTwoPhaseEulerFoam` solver, but should work for any Eulerian solver provided the field names are specfied correctly in the `fvOptions` dictionaries. For `reactingTwoPhaseEulerFoam` the only entries that need to be changed are the `patches` entries in each of the `degassingMassSource` and `degassingForce` dictionaries. The `patches` entry must specify the name(s) of the boundary patches where the degassing boundary is applied. The folder `tutorial` contains a bubble column case that uses this boundary condition. 
