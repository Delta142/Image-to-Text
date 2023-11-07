import numpy as np
import math

from Tools import ImgeEyesExtractor as IMGProc

#Cosntants for Algorithm
#define file Arr
FilesNames = ['Train_data/Letters/TrainSet1', 'Train_data/Letters/TestSet1']
#Layer config
LayerConfig = [784, 28, 1]
#Learning rate 
LearnR = 0.2
#Amount of times to loop through data to garantee training 
TrainIterations = 10

Files = ['0-1 Test Set', '0-4 Test Set', '0-1 Train Set', '0-4 training set']


def sigmoid(x):
    #fixes overflow?
    x = np.clip(x, -500, 500)
    return 1/(1+math.pow(math.e,-x))

def InverseSig(x):

    return  x * (1- x)
    

def readfile(fileName):
   pass

def Train(Correct ,Data ,Bias ,Weights ):
    
    W_H = Weights[0]
    W_O = Weights[1]

    #print(len(W_H))

    B_H = Bias[0]
    B_O = Bias[1]

    #print(W_O)
    for j in range(TrainIterations):
        for i in range(len(Data)):
            #print(i)    
            # Forward
            H_in = np.dot(list(np.array(W_H).transpose()), Data[i])
            H_in = np.add(B_H, H_in)
            H_Layer = list(map(sigmoid, H_in))

            H_o = np.dot(np.array(W_O).transpose(), H_Layer)
            H_o = np.add(B_O, H_o)
            Out = list(map(sigmoid, H_o))
            ##########
            
            # BackPropagate
            Delta_O = (Correct[i] - Out[0]) * InverseSig(Out[0])
            Delta_H = np.multiply((np.array(np.dot(W_O, Delta_O)).transpose())[0], list(map(InverseSig, H_Layer)))
        
            W_O = np.add((np.array(W_O).transpose())[0], np.multiply(LearnR, np.dot(H_Layer, Delta_O)))
            B_O = np.add(B_O, np.multiply(LearnR, Delta_O))
            W_H = np.add(W_H, np.multiply(LearnR, np.outer(Data[i], Delta_O)))
            B_H = np.add(B_H, np.multiply(LearnR, Delta_H))


    
        print("Epoch, ", j, " Has concluded")
    
    Bi_N = [B_H,B_O]
    We_N = [W_H,W_O]
    
    #print(W_O)
    return [Bi_N,We_N]
    #print(len(BBBW_H))
        

def Test(Correct ,Data ,Bias ,Weights):
        
    W_H = Weights[0]
    W_O = Weights[1]

    B_H = Bias[0]
    B_O = Bias[1]

    count = 0

    for i in range(len(Data)):
        H_in = np.dot(list(np.array(W_H).transpose()), Data[i])
        H_in = np.add(B_H, H_in)
        H_Layer = list(map(sigmoid, H_in))

        H_o = np.dot(np.array(W_O).transpose(), H_Layer)
        H_o = np.add(B_O, H_o)
        Out = list(map(sigmoid, H_o))
        
        if (Out[0] >= 0.5):
            ans = 1
        else:
            ans = 0

        if (ans == Correct[i]):
            count += 1
        else:
            print("Element ",i, "| Out ", Out, "| ans", Correct[i])

    print("Total Correct: ", count)
    print("Accuracy:      ", count/(len(Correct)))

def prepare(fileChoice):
    print("\n")
    StdrdArr = readfile(FilesNames[fileChoice])
    #[1x1]*N
    Ans = [] #The correct answer
    #[1x784]*N
    Pic = [] #The image as 1's and zeros

    Weights_L0_L1 = [] # weights for layer 0 -> 1
    Weights_L1_L2 = [] # weights for layer 1 -> 2
    Bias_L0_L1 = []
    Bias_L1_L2 = []
    #weight creation
    for i in range(LayerConfig[0]):
        Weights_L0_L1.append(list(np.random.uniform(-1,1,LayerConfig[1])))
    
    for i in range(LayerConfig[1]):
        Weights_L1_L2.append(list(np.random.uniform(-1,1,LayerConfig[2])))

    Bias_L0_L1 = (list(np.random.uniform(-1,1,(LayerConfig[1]))))
    Bias_L1_L2 = (list(np.random.uniform(-1,1,(LayerConfig[2]))))

    Bias    = [Bias_L0_L1, Bias_L1_L2]
    Weights = [Weights_L0_L1, Weights_L1_L2]

    for i in StdrdArr:
        Ans.append(i.pop(0))
        Pic.append(i)

    return [Ans, Pic, Bias, Weights]

Prep_INPT = prepare(2)

Ans_arr  = Prep_INPT[0]
Data_arr = Prep_INPT[1]
Bias_arr = Prep_INPT[2]
Weights_arr  = Prep_INPT[3]
            #[B, W]
NewTrained = Train(Ans_arr,Data_arr,Bias_arr,Weights_arr)

NewBias    = NewTrained[0]
NewWeights = NewTrained[1]

# test on real set
trash = Prep_INPT = prepare(0)

Ans_arr  = Prep_INPT[0]
Data_arr = Prep_INPT[1]

Test(Ans_arr,Data_arr, NewBias, NewWeights)