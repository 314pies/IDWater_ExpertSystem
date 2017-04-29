#include<bits/stdc++.h>


using namespace std;

int main()
{
    fstream dataFile;
    fstream TrainFile;
    dataFile.open("data.txt",ios::in);
    TrainFile.open("trainData.csv");

    float testValue;
    int Q1,Q2,Q3,Q4;
    while(dataFile>>testValue>>Q1>>Q2>>Q3>>Q4)
    {
        char Result='X';
        if(testValue >=3)
        {
            if(Q3 == 1)
            {
                Result = 'F';
            }
            else if(Q4 == 1)
            {
                Result = 'M';
            }
            else if(Q1 == 1)
            {
                Result = 'W';
            }
            else  if(Q2==1)
            {
                Result = 'W';
            }
        }
        else if(testValue>=2)
        {
            if(Q3==1) //0
            {
                Result = 'F';
            }
            else if(Q1 == 1)  //0
            {
                Result = 'W';
            }
            else if(Q2 == 1)  //1
            {
                Result = 'W';
            }
            else if(Q4 == 1) //1
            {
                Result = 'M';
            }
        }else{
            Result = 'N';
        }

        TrainFile<<Result<<","<<testValue<<","<<Q1<<","<<Q2<<","<<Q3<<","<<Q4<<endl;
    }
}
