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
#line 32 "/home/parallels/OpenFOAM/parallels-9/run/finalProject/simulations/run016/constant/fvModels/degassingMassSource"
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
    // SHA1 = 960c29cddea75cf6f5b35e827dcdaee5ff3dcf64
    //
    // unique function name that can be checked if the correct library version
    // has been loaded
    void degassingMassSource_960c29cddea75cf6f5b35e827dcdaee5ff3dcf64(bool load)
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

defineTypeNameAndDebug(degassingMassSourceFvModelscalarSource, 0);

addRemovableToRunTimeSelectionTable
(
    fvModel,
    degassingMassSourceFvModelscalarSource,
    dictionary
);


const char* const degassingMassSourceFvModelscalarSource::SHA1sum =
    "960c29cddea75cf6f5b35e827dcdaee5ff3dcf64";


// * * * * * * * * * * * * * * * * Constructors  * * * * * * * * * * * * * * //

degassingMassSourceFvModelscalarSource::
degassingMassSourceFvModelscalarSource
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
        Info<<"construct degassingMassSource sha1: 960c29cddea75cf6f5b35e827dcdaee5ff3dcf64"
            " from components\n";
    }
}


// * * * * * * * * * * * * * * * * Destructor  * * * * * * * * * * * * * * * //

degassingMassSourceFvModelscalarSource::
~degassingMassSourceFvModelscalarSource()
{
    if (false)
    {
        Info<<"destroy degassingMassSource sha1: 960c29cddea75cf6f5b35e827dcdaee5ff3dcf64\n";
    }
}


// * * * * * * * * * * * * * * * Member Functions  * * * * * * * * * * * * * //

void degassingMassSourceFvModelscalarSource::addSup
(
    fvMatrix<scalar>& eqn,
    const word& fieldName
) const
{
    if (false)
    {
        Info<<"degassingMassSourceFvModelscalarSource::addSup()\n";
    }

//{{{ begin code
    
//}}} end code
}


void degassingMassSourceFvModelscalarSource::addSup
(
    const volScalarField& rho,
    fvMatrix<scalar>& eqn,
    const word& fieldName
) const
{
    if (false)
    {
        Info<<"degassingMassSourceFvModelscalarSource::addSup()\n";
    }

//{{{ begin code
    #line 37 "/home/parallels/OpenFOAM/parallels-9/run/finalProject/simulations/run016/constant/fvModels/degassingMassSource"
Info << "**codeAddSup**" << endl;
    	 
    	 
         // Get the names of the patches on which to apply the degassing forces
         DynamicList<word, 1, 0> patches;
         coeffs().lookup("patches") >> patches;

         // Get the required fields
         const word rhoName = coeffs().lookup("rhoName");
         const volScalarField& rhoAir = mesh().lookupObject<volScalarField>(rhoName);
         const word alphaName = coeffs().lookup("alphaName");
         const volScalarField& alphaAir = mesh().lookupObject<volScalarField>(alphaName);

         // Get the timestep
         const scalar deltaT = mesh().time().deltaT().value();

         // Create degassing mass source coefficient and initialize to zero
         volScalarField degassingMassSourceCoeff
         (
             IOobject
             (
                 "degassingMassSourceCoeff",
                 mesh().time().timeName(),
                 mesh(),
                 IOobject::NO_READ,
                 IOobject::AUTO_WRITE
             ),
             mesh(),
             dimensionedScalar("degassingMassSourceCoeff", dimless/dimTime, 0.0)
         );

         // Compute the degassing mass source coefficient for each cell adjacent to the selected patches
         forAll(patches, iPatch)
         {
             // Get the boundary patch
             const fvPatch& patch = mesh().boundary()[patches[iPatch]];

             // Loop through each boundary face and compute degassing force coefficient in adjacent cell
             forAll(patch, iFace)
             {
                 label iCell = patch.faceCells()[iFace];
                 degassingMassSourceCoeff[iCell] = -alphaAir[iCell]/deltaT;
             }
         }

         // Add the degassing force term
         eqn += fvm::Sp(degassingMassSourceCoeff, rhoAir);
//}}} end code
}


void degassingMassSourceFvModelscalarSource::addSup
(
    const volScalarField& alpha,
    const volScalarField& rho,
    fvMatrix<scalar>& eqn,
    const word& fieldName
) const
{
    if (false)
    {
        Info<<"degassingMassSourceFvModelscalarSource::addSup()\n";
    }

//{{{ begin code
    
//}}} end code
}


// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

} // End namespace Foam
} // End namespace fv

// ************************************************************************* //

