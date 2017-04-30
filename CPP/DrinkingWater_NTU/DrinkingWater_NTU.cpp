#include<bits/stdc++.h>


using namespace std;

int main()
{
    fstream dataFile;
    fstream TrainFile;
    dataFile.open("data.txt",ios::in);
    TrainFile.open("trainData.csv");

    float testValue;
    int day;
    int Q1;
    while(dataFile>>testValue>>day>>Q1)
    {
        string Result="X";
        if(testValue <=2)
        {
            Result = "N";
        }
        else if(testValue>2)
        {
            if(Q1 == 1)
            {
                Result = "D";
            }
            else if(day>90)
            {
                Result = "C";
            }else{
                Result = "CA";
            }
        }

        TrainFile<<Result<<","<<testValue<<","<<day<<","<<Q1<<endl;
    }
}
