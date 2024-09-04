// This is pseudocode



#include<stdio.h>

int knownweight=100;

int calibrate(weightreading){
// here we can calibrate the sensor if needed 
//like the weight sensor having the strain gauges which need to calibrate with known weights
int calibrated_value=weightreading/knownweight;  // formula is depends on the sensor 
return calibrated_value;
}

int validate(pirreading){
    int count=0;
    //here we can use the counter based approch to insure the correctness 
    //like PIR sensor used to detect the human presence 
    if(count>=20){
        return 1;
    }
    else{
        count=0;
        return 0;
    }
    if(pirreading==1){
        count+=1;
    }
    
    
}
void loop(){


int pirreading=readpir();//assume that this readpir function will read the pir sensor data
if(validate(pirreading)){
    printf("Human Presence Detected");
}


int weightreading=readweight();//assume that this readweight function will read the weight sensor data
int actualweight=calibrate(weightreading);
print("weight=%d",actualweight);

}
