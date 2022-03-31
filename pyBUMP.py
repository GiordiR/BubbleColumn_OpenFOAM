import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os

def readScalar(caseFolder, sampleType, fileName):
    
    #Find sample path
    sampleTypePath = os.path.join(caseFolder, "postProcessing", sampleType)
    samplePath = os.path.join(sampleTypePath, os.listdir(sampleTypePath)[0], fileName)  
    
    #Read sample file and sort                 
    varDf = pd.read_csv(samplePath, delimiter="\s+", skiprows=2, header=None)
    vars = varDf.to_numpy(dtype=float)
    vars = vars[np.argsort(vars[:, 0])]
    
    #Mean over equal x values
    avgVars = np.average(vars[:,3].reshape(-1, 4), axis=1)
    
    #x values
    xVars = vars[::4, 0]
    
    return xVars, avgVars


def plot(xVar, yVar):
    
    fig = plt.figure()
    ax = fig.subplots()
    ax.plot(xVar, yVar, label = 'test')
    ax.set_title('test')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    plt.show()

