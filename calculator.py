import random
import datetime
import testfunction
print("**************************************************");
print("*                                                *");
print("*   Python function time complexity calculator   *");
print("*                                                *");
print("*      A program by Billy Li and Ricky Peng      *");
print("*                                                *");
print("* Instructions:                                  *");
print("*   1. paste your functions that you wish to     *");
print("* test into the 'testfunction.py' file.          *");
print("*   2. Follow the prompts and enter information  *");
print("* about your function's parameters.              *");
print("*   3. The functions should have its scaling     *");
print("* parameter (the one O(N) calculations are based *");
print("* on) as its first parameter: e.g:               *");
print("*   def function(scale,constant)                 *");
print("*   4. Read the test result.                     *");
print("*                                                *");
print("*                   Have fun!                    *");
print("*                                                *");
print("**************************************************");
print("");

#Function parameters
while(True):
        functionName = input("Please enter the name of your function:");
        print("**************************************************");
        print("Please enter the number of parameters of your function:");
        inputNumber = input("");
        while (True):
                try:
                        inputNumber = int(inputNumber);
                except ValueError:
                        pass;
                if isinstance(inputNumber,int):
                        if int(inputNumber) > 0:
                                break;
                print("Please enter an integer greater than 0.");
                inputNumber = input("");
                try:
                        inputNumber = int(inputNumber);
                except ValueError:
                        pass;
                
        #Parameter types
        print("**************************************************");
        print("Please enter your input type as a number:");
        print("List: 1, Integer: 2, String: 3");
        inputType = [0] * inputNumber;
        for i in range (0, len(inputType)):
                print("Please specify the input type of parameter "+str(i+1)+":");
                inputType[i] = input("");
                while (True):
                        try:
                                inputType[i] = int(inputType[i]);
                        except ValueError:
                                pass;
                        if isinstance(inputType[i],int):
                                if (int(inputType[i]) > 0 and int(inputType[i]) < 4):
                                        break;
                        print("Please enter an integer between 1 and 3.");
                        inputType[i] = input("");
                        try:
                                inputType[i] = int(inputType[i]);
                        except ValueError:
                                pass;
        arrayType = [None] * inputNumber;

        #List contents
        for i in range (0, len(inputType)):
                if (inputType[i] == 1):
                        print("**************************************************");
                        print("You have specified parameter "+str(i+1)+" to be a list.");
                        print("What types of values does it contain?");
                        print("Integer: 2, String: 3");
                        arrayType[i] = input("");
                        while (True):
                                try:
                                        arrayType[i]  = int(arrayType[i]);
                                except ValueError:
                                        pass;
                                if isinstance(arrayType[i],int):
                                        if (int(arrayType[i]) > 1 and int(arrayType[i]) < 5):
                                                break;
                                print("Please enter an integer between 2 and 3.");
                                arrayType[i] = input("");
                                try:
                                        arrayType[i] = int(arrayType[i]);
                                except ValueError:
                                        pass;

        #Parameter range
        inputRange = [(None,None)] * inputNumber;
        for i in range(1, len(inputRange)):
                print("**************************************************");
                print("Enter the lower bound of parameter "+str(i+1)+"'s value/length. The bound is inclusive.");
                lower = input("");
                while (True):
                        try:
                                lower = int(lower);
                        except ValueError:
                                pass;
                        if isinstance(lower,int):
                                break;
                        print("Please enter an integer.");
                        lower = input("");
                        try:
                                lower = int(lower);
                        except ValueError:
                                pass;
                print("**************************************************");
                print("Enter the upper bound of parameter "+str(i+1)+"'s value/length. The bound is inclusive.");
                upper = input("");
                while (True):
                        try:
                                upper = int(upper);
                        except ValueError:
                                pass;
                        if isinstance(upper,int):
                                break;
                        print("Please enter an integer.");
                        upper = input("");
                        try:
                                upper = int(upper);
                        except ValueError:
                                pass;
                inputRange[i] = (lower,upper);
        arrayRangeValue = [(None,None)]*inputNumber;

        #List content range
        for i in range (0, len(inputType)):
                if (inputType[i] == 1):
                        print("**************************************************");
                        print("Enter the lower bound of list "+str(i+1)+"'s contents' value/length. The bound is inclusive.");
                        lower = input("");
                        while (True):
                                try:
                                        lower = int(lower);
                                except ValueError:
                                        pass;
                                if isinstance(lower,int):
                                        break;
                                print("Please enter an integer.");
                                lower = input("");
                                try:
                                        lower = int(lower);
                                except ValueError:
                                        pass;
                        print("**************************************************");
                        print("Enter the upper bound of list "+str(i+1)+"'s contents' value/length. The bound is inclusive.");
                        upper = input("");
                        while (True):
                                try:
                                        upper = int(upper);
                                except ValueError:
                                        pass;
                                if isinstance(upper,int):
                                        break;
                                print("Please enter an integer.");
                                upper = input("");
                                try:
                                        upper = int(upper);
                                except ValueError:
                                        pass;
                        arrayRangeValue[i] = (lower,upper);

        #exception handling
        power = 2;
        try:
                if (inputType[0] == 1):
                        if(arrayType[0] == 2):
                                testData = [];
                                for i in range (0,2**power):
                                        testData.append(random.randint(arrayRangeValue[0][0],arrayRangeValue[0][1]));
                        else:
                                testData = [];
                                for i in range (0, 2**power):
                                        length = random.randint(arrayRangeValue[0][0],arrayRangeValue[0][1]);
                                        testString = "";
                                        for j in range(0,length):
                                                testString = testString + chr(random.randint(97,122));
                                        testData.append(testString);
                                
                elif (inputType[0] == 2):
                        testData = 2**power;
                else:
                        testData = "";
                        for j in range(0,2**power):
                                testData = testData + chr(random.randint(97,122));

                #generate input for other variables
                otherTest = [];
                for other in range (1,inputNumber):
                        if (inputType[other] == 1):
                                if(arrayType[other] == 2):
                                        testDataOther = [];
                                        arrayRange = random.randint(inputRange[other][0],inputRange[other][1]);
                                        for i in range (0,arrayRange):
                                                testDataOther.append(random.randint(arrayRangeValue[other][0],arrayRangeValue[other][1]));
                                else:
                                        testDataOther = [];
                                        arrayRange = random.randint(inputRange[other][0],inputRange[other][1]);
                                        for i in range (0, arrayRange):
                                                length = random.randint(arrayRangeValue[other][0],arrayRangeValue[other][1]);
                                                testString = "";
                                                for j in range(0,length):
                                                        testString = testString + chr(random.randint(97,122));
                                                testDataOther.append(testString);                                
                        elif (inputType[other] == 2):
                                testDataOther = random.randint(inputRange[other][0],inputRange[other][1]);
                        else:
                                testDataOther = "";
                                stringRange = random.randint(inputRange[other][0],inputRange[other][1]);
                                for j in range(0,stringRange):
                                        testDataOther = testDataOther + chr(random.randint(97,122));
                        otherTest.append(testDataOther);
                        
                #running test results with function
                #building test string
                if len(otherTest) == 0:
                        programString = "testfunction."+functionName+"(testData);"
                else:
                        programString = "testfunction."+functionName+"(testData"
                        for i in range(0,len(otherTest)):
                                programString = programString + ",otherTest["+str(i)+"]";
                        programString = programString + ");"
                exec(programString);
                break;
        except:
                print("**************************************************");
                print("An error occured in your test function; please double check the information you entered.");
                print("**************************************************");
#Test
print("**************************************************");
print("**************************************************");
print("Generating test input; this may take a while.");
timeTaken = [];
timePower = [];
currentTime = [0]*3;
averageTime = 0;
power = 1;
while(averageTime < 2.5):
        for c in range (0,3):
                
                #generate input for scaling variable
                if (inputType[0] == 1):
                        if(arrayType[0] == 2):
                                testData = [];
                                for i in range (0,2**power):
                                        testData.append(random.randint(arrayRangeValue[0][0],arrayRangeValue[0][1]));
                        else:
                                testData = [];
                                for i in range (0, 2**power):
                                        length = random.randint(arrayRangeValue[0][0],arrayRangeValue[0][1]);
                                        testString = "";
                                        for j in range(0,length):
                                                testString = testString + chr(random.randint(97,122));
                                        testData.append(testString);
                                
                elif (inputType[0] == 2):
                        testData = 2**power;
                else:
                        testData = "";
                        for j in range(0,2**power):
                                testData = testData + chr(random.randint(97,122));

                #generate input for other variables
                otherTest = [];
                for other in range (1,inputNumber):
                        if (inputType[other] == 1):
                                if(arrayType[other] == 2):
                                        testDataOther = [];
                                        arrayRange = random.randint(inputRange[other][0],inputRange[other][1]);
                                        for i in range (0,arrayRange):
                                                testDataOther.append(random.randint(arrayRangeValue[other][0],arrayRangeValue[other][1]));
                                else:
                                        testDataOther = [];
                                        arrayRange = random.randint(inputRange[other][0],inputRange[other][1]);
                                        for i in range (0, arrayRange):
                                                length = random.randint(arrayRangeValue[other][0],arrayRangeValue[other][1]);
                                                testString = "";
                                                for j in range(0,length):
                                                        testString = testString + chr(random.randint(97,122));
                                                testDataOther.append(testString);                                
                        elif (inputType[other] == 2):
                                testDataOther = random.randint(inputRange[other][0],inputRange[other][1]);
                        else:
                                testDataOther = "";
                                stringRange = random.randint(inputRange[other][0],inputRange[other][1]);
                                for j in range(0,stringRange):
                                        testDataOther = testDataOther + chr(random.randint(97,122));
                        otherTest.append(testDataOther);
                        
                #running test results with function
                #building test string
                if len(otherTest) == 0:
                        programString = "testfunction."+functionName+"(testData);"
                else:
                        programString = "testfunction."+functionName+"(testData"
                        for i in range(0,len(otherTest)):
                                programString = programString + ",otherTest["+str(i)+"]";
                        programString = programString + ");"

                #starting timer
                timeStart = datetime.datetime.now();
                exec(programString);
                timeStart = timeStart.timestamp();
                timeEnd = datetime.datetime.now();
                timeEnd = timeEnd.timestamp();
                currentTime[c] = timeEnd-timeStart;
        averageTime = (currentTime[0]+currentTime[1]+currentTime[2])/3;
        if(averageTime > 0.02):
                timeTaken.append(averageTime);
                timePower.append(power);
                print("time taken for data size "+str(2**power)+": "+str(averageTime)+" seconds");
        power = power + 1;

#interpreting test result: calculating increase in time for every doubling of data size
steps = [];
logFactor = 0;
for i in range(1,len(timeTaken)):
        steps.append(timeTaken[i]/timeTaken[i-1]);
        logFactor = logFactor + timePower[i]/timePower[i-1];
logFactor = (logFactor) / (len(timeTaken)-1);
averageStep = 0;

#calculate average increase
for i in range(0,len(steps)):
        averageStep = averageStep + steps[i];
averageStep = averageStep / len(steps);
print("Average time increase per doubling of data size:"+str(averageStep));

#separate polynomial and log factors
polynomial = 0;
logarithmic = 0;
while (averageStep >1.95):
        averageStep = averageStep / 2;
        polynomial = polynomial + 1;
while (averageStep > logFactor - 0.01):
        averageStep = averageStep / logFactor;
        logarithmic = logarithmic + 1;

#generating test string
polyString = "";
logString = "";
if polynomial > 0:
        polyString = polyString + "N";
if polynomial > 1:
        polyString = polyString + "^"+str(polynomial);
if logarithmic > 0:
        logString = logString + "logN";
if logarithmic > 1:
        logString = "("+logString+")" + "^"+str(logarithmic);
if ((polynomial == 0) and (logarithmic == 0)):
        print("The test function is of time complexity 0(1).");
else:
        print("The test function is of time complexity 0("+polyString+logString+").");
input("Testing finished. press enter to close.");
