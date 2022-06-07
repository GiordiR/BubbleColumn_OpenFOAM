/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
   \\    /   O peration     | Website:  https://openfoam.org
    \\  /    A nd           | Copyright (C) YEAR OpenFOAM Foundation
     \\/     M anipulation  |
-------------------------------------------------------------------------------
License
    This file is part of OpenFOAM.

    OpenFOAM is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenFOAM is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

    You should have received a copy of the GNU General Public License
    along with OpenFOAM.  If not, see <http://www.gnu.org/licenses/>.

\*---------------------------------------------------------------------------*/

#include "codedFvModelTemplate.H"
#include "addToRunTimeSelectionTable.H"
#include "fvPatchFieldMapper.H"
#include "volFields.H"
#include "surfaceFields.H"
#include "unitConversion.H"
#include "fvMatrix.H"

//{{{ begin codeInclude
#line 111 "/global-scratch/bulk_pool/spassoni/OFproject/run014/constant/fvModels/degassingForce"
#include "fvm.H"
//}}} end codeInclude


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

namespace Foam
{

namespace fv
{

// * * * * * * * * * * * * * * * Local Functions * * * * * * * * * * * * * * //

//{{{ begin localCode

//}}} end localCode


// * * * * * * * * * * * * * * * Global Functions  * * * * * * * * * * * * * //

extern "C"
{
    // dynamicCode:
    // SHA1 = 4bd3fe1d896dfa2d0533e1403e34537849a04154
    //
    // unique function name that can be checked if the correct library version
    // has been loaded
    void degassingForce_4bd3fe1d896dfa2d0533e1403e34537849a04154(bool load)
    {
        if (load)
        {
            // code that can be explicitly executed after loading
        }
        else
        {
            // code that can be explicitly executed before unloading
        }
    }
}

// * * * * * * * * * * * * * * Static Data Members * * * * * * * * * * * * * //

defineTypeNameAndDebug(degassingForceFvModelvectorSource, 0);

addRemovableToRunTimeSelectionTable
(
    fvModel,
    degassingForceFvModelvectorSource,
    dictionary
);


const char* const degassingForceFvModelvectorSource::SHA1sum =
    "4bd3fe1d896dfa2d0533e1403e34537849a04154";


// * * * * * * * * * * * * * * * * Constructors  * * * * * * * * * * * * * * //

degassingForceFvModelvectorSource::
degassingForceFvModelvectorSource
(
    const word& name,
    const word& modelType,
    const dictionary& dict,
    const fvMesh& mesh
)
:
    fvModel(name, modelType, dict, mesh),
    set_(coeffs(), mesh)
{
    if (false)
    {
        Info<<"construct degassingForce sha1: 4bd3fe1d896dfa2d0533e1403e34537849a04154"
            " from components\n";
    }
}


// * * * * * * * * * * * * * * * * Destructor  * * * * * * * * * * * * * * * //

degassingForceFvModelvectorSource::
~degassingForceFvModelvectorSource()
{
    if (false)
    {
        Info<<"destroy degassingForce sha1: 4bd3fe1d896dfa2d0533e1403e34537849a04154\n";
    }
}


// * * * * * * * * * * * * * * * Member Functions  * * * * * * * * * * * * * //

void degassingForceFvModelvectorSource::addSup
(
    fvMatrix<vector>& eqn,
    const word& fieldName
) const
{
    if (false)
    {
        Info<<"degassingForceFvModelvectorSource::addSup()\n";
    }

//{{{ begin code
    
//}}} end code
}


void degassingForceFvModelvectorSource::addSup
(
    const volScalarField& rho,
    fvMatrix<vector>& eqn,
    const word& fieldName
) const
{
    if (false)
    {
        Info<<"degassingForceFvModelvectorSource::addSup()\n";
    }

//{{{ begin code
    #line 116 "/global-scratch/bulk_pool/spassoni/OFproject/run014/constant/fvModels/degassingForce"
// Get the names of the patches on which to apply the degassing forces
         DynamicList<word, 1, 0> patches;
         coeffs().lookup("patches") >> patches;

         // Get the required fields
         const word rhoName = coeffs().lookup("rhoName");
         const volScalarField& rhoAir = mesh().lookupObject<volScalarField>(rhoName);
         const word alphaName = coeffs().lookup("alphaName");
         const volScalarField& alphaAir = mesh().lookupObject<volScalarField>(alphaName);
         const word UName = coeffs().lookup("UName");
         const volVectorField& UAir = mesh().lookupObject<volVectorField>(UName);

         // Get the timestep
         const scalar deltaT = mesh().time().deltaT().value();

         // Create degassing force coefficient and initialize to zero
         volScalarField degassingForceCoeff
         (
             IOobject
             (
                 "degassingForceCoeff",
                 mesh().time().timeName(),
                 mesh(),
                 IOobject::NO_READ,
                 IOobject::AUTO_WRITE
             ),
             mesh(),
             dimensionedScalar("degassingForceCoeff", dimDensity/dimTime, 0.0)
         );

         // Compute the degassing force coefficient for each cell adjacent to the selected patches
         forAll(patches, iPatch)
         {
             // Get the boundary patch
             const fvPatch& patch = mesh().boundary()[patches[iPatch]];

             // Loop through each boundary face and compute degassing force coefficient in adjacent cell
             forAll(patch, iFace)
             {
                 label iCell = patch.faceCells()[iFace];
                 degassingForceCoeff[iCell] = -rhoAir[iCell]*alphaAir[iCell]/deltaT;
             }
         }

         // Add the degassing force term
         eqn += fvm::Sp(degassingForceCoeff, UAir);
//}}} end code
}


void degassingForceFvModelvectorSource::addSup
(
    const volScalarField& alpha,
    const volScalarField& rho,
    fvMatrix<vector>& eqn,
    const word& fieldName
) const
{
    if (false)
    {
        Info<<"degassingForceFvModelvectorSource::addSup()\n";
    }

//{{{ begin code
    
//}}} end code
}


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

} // End namespace Foam
} // End namespace fv

// ************************************************************************* //

