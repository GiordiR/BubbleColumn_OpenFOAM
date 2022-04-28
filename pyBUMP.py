import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os

def readScalar(caseFolder, sampleType, fileName, nz=4, instantaneous=False, dt=0.05):
    
    #Find sample path
    sampleTypePath = os.path.join(caseFolder, "postProcessing", sampleType)
    samplePath = os.path.join(sampleTypePath, findMaxTimeFolder(sampleTypePath), fileName)  
    
    #Find data firs line
    iRow = findFirstRow(samplePath)
    
    #Read sample file and sort                 
    varDf = pd.read_csv(samplePath, delimiter="\s+", skiprows=iRow, header=None)
    vars = varDf.to_numpy(dtype=float)
    
    if sampleType=="surfaces":
        #Sort data
        vars = vars[np.argsort(vars[:, 0])]
        
        #Mean over equal x values
        yVars = np.average(vars[:,3].reshape(-1, nz), axis=1)
        
        #x values
        xVars = vars[::nz, 0]
        
    elif sampleType=="holdUp":
        if instantaneous==True:
            xVars = vars[:,0]
            yVars = vars[:,1]
        else:
            xVars = vars[int(30/dt)::,0]
            yVars = cum_mean(vars[int(30/dt)::,1])          
            #print("Time-averaged gas holdup = " + str(yVars[-1]))
    return xVars, yVars

def readExpData(fileName):
    
    dataDf = pd.read_excel(fileName, engine='openpyxl', skiprows=4)
    data = {'J6h8': dataDf.to_numpy(dtype=float)[:,:3],
            'J8h8' : dataDf.to_numpy(dtype=float)[:,3:6],
            'J10h8' : dataDf.to_numpy(dtype=float)[:-1,6:9],
            'J6h63' : dataDf.to_numpy(dtype=float)[:,10:13],
            'J8h63' : dataDf.to_numpy(dtype=float)[:,13:16],
            'J10h63' : dataDf.to_numpy(dtype=float)[:,16:19]}
    
    return data

def findExpData(J,h):
    pass

def findFirstRow(filePath):
    
    with open(filePath) as file:
        i = 0
        lines = file.readlines()
        for line in lines:
            if not line.startswith("#"):
                break
            i += 1

    return i

def findMaxTimeFolder(folderPath):
    
    folderList = os.listdir(folderPath)
    folderArray = [int(x) for x in folderList]
       
    return str(max(folderArray))

def cum_mean(arr):
    cum_sum = np.cumsum(arr, axis=0)    
    for i in range(cum_sum.shape[0]):       
        if i == 0:
            continue        
        cum_sum[i] =  cum_sum[i] / (i + 1)
    
    return cum_sum

def write_holdup(yVars,save_path):
    with open(save_path+"global_holdup.txt",'a+'):
        pass
    

def plot(figID, xVars, yVars, sampleType, J, h, label, caso="mesh", lastCompare=True):
    
    save_path=os.path.join("./graphs", caso)
    if not os.path.isdir(save_path):
        os.makedirs(save_path)
    # Import experimental data
    expDataDict = readExpData("Krepper_expData.xlsx")
    expData = expDataDict['J'+str(J)+'h'+str(h)]
    
    # Create figure
    plt.figure(figID, figsize=[20,10])
    
    if sampleType=="surfaces":   
        xNorm = xVars/max(xVars)
        plt.plot(xNorm, yVars, 'o', label = label + r" - $J_G$ = "+str(J)+" mm/s", linestyle="--")
        plt.title('Gas volume fraction distribution at h = '+str(h)+' cm')
        plt.xlabel('x/L (-)')
        plt.ylabel('gas volume fraction (-)')
        plt.grid(which='both', alpha=0.3)
        if h==8:
            plt.xlim(0,1.025)
            plt.ylim(0,0.06)
        if h==63:
            plt.xlim(0,1.025)
            plt.ylim(0.03,0.055)
        plt.xticks(np.arange(0,1.025,0.1))
        if lastCompare==True:
            plt.plot(expData[:,1], expData[:,2], 'o', label=r"experimental - $J_G$ = "+str(J)+" mm/s", linestyle="--")
            plt.legend()
            plt.savefig(save_path+'/surfacesJ'+str(J)+'h'+str(h)+'.png')
            plt.close() 
        
    elif sampleType=="holdUp":
        plt.plot(xVars, yVars, label = label + r" - $J_G$ = "+str(J)+" mm/s")
        if lastCompare==True:
            plt.legend()
            plt.title('Global gas holdup')
            plt.xlabel('Time (s)')
            plt.ylabel('gas holdup (-)')
            plt.grid(which='both', alpha=0.3)  
        plt.savefig(save_path+'/holdUp'+str(J)+'.png')
        
    elif sampleType=="holdUpInstantaneous":
        plt.plot(xVars, yVars, label = label + r" - $J_G$ = "+str(J)+" mm/s")
        if lastCompare==True:
            plt.legend()
            plt.title('Instantaneous global gas holdup')
            plt.xlabel('Time (s)')
            plt.ylabel('gas holdup (-)')
            plt.grid(which='both', alpha=0.3)   
        plt.savefig(save_path+'/holdUpInstantaneous'+str(J)+'.png')
        
    else:
        print("Error! no such sample type!")


