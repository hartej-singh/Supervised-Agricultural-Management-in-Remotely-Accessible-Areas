// import the GSM library
#include <GSM.h>

// PIN Number
#define PINNUMBER ""

// initialize the library instance

GSM gsmAccess(true);     // include a 'true' parameter for debug enabled

GSMScanner scannerNetworks;

GSMModem modemTest;

// Save data variables

String IMEI = "";

// serial monitor result messages

String errortext = "ERROR";

String m="";
int ON = 8; // ON is for dehumidifer (analog port)
int S=A0; // humidity sensor
int Pump=6; // water pump to fill the water tanker
int Threshold = ; // for humidity



// We can water the plants every 3 hrs with 50 ml of water to maintain the water levels, keeping in mind this effects the humidity.
int Actuator=5; //actuator is controlled from port 5
int Time=0;

void setup()
{
    // initialize the ON pinmode for the dehumidifier

    pinMode(ON,OUTPUT);  // Dehumidifier
    pinMode(Pump,OUTPUT); // Water Pump
    pinMode(Actuator,OUTPUT) // Plant Watering actuator, gives 50 ml to the plants in one watering.
    pinMode(S,INPUT); // Humidity sensor readings
    pinMode(A1,INPUT); // The Water Depth Sensor is connected to the A1 analog pin

    // initialize serial communications

    Serial.begin(9600);

    Serial.println("GSM networks scanner");

    scannerNetworks.begin();

    // connection state

    boolean notConnected = true;

    // Start GSM shield

    // If your SIM has PIN, pass it as a parameter of begin() in quotes

    while(notConnected)

    {

        if(gsmAccess.begin(PINNUMBER)==GSM_READY)

            notConnected = false;

        else

        {

            Serial.println("Not connected");

            delay(1000);

        }

    }

    // get modem parameters

    // IMEI, modem unique identifier

    Serial.print("Modem IMEI: ");

    IMEI = modemTest.getIMEI();

    IMEI.replace("\n","");

    if(IMEI != NULL)

        Serial.println(IMEI);

    // currently connected carrier

    Serial.print("Current carrier: ");

    Serial.println(scannerNetworks.getCurrentCarrier());

    // returns strength and ber

    // signal strength in 0-31 scale. 31 means power > 51dBm

    // BER is the Bit Error Rate. 0-7 scale. 99=not detectable

    Serial.print("Signal Strength: ");

    Serial.print(scannerNetworks.getSignalStrength());

    Serial.println(" [0-31]");
}

void loop()
{
    // Send or Recieve Messages
    if (Serial.available()>0)
        switch(Serial.read())
        {
        case 's':
            SendMessage();
            break;
        case 'r':
            RecieveMessage();
            break;
        }
    m=analogRead(S);
    if(m<Threshold)
    {
        digitalWrite(ON,HIGH);
        delay(3000000);
        digitalWrite(ON,LOW);
        Time=Time+300; // delay of 5 minute for the
    }
    else
    {
        digitalWrite(ON,LOW);
    }
    d=analogRead(A1);
    if(d<minDepth)
    {
        digitalWrite(Pump,HIGH);
    }
    else
    {
        digitalWrite(Pump,LOW);
    }
    if(Time==0)
    {
        Time=Time+1;
        delay(1000);
        digitalWrite(Actuator,LOW);
    }
    else
    {
        if(Time==10800)
        {
            digitalWrite(Actuator,HIGH);
            Time=0;
            delay(60000);
            Time=Time+60;
        }
        else
        {
            Time=Time+1;
            delay(1000);
        }
    }

    // scan for existing networks, displays a list of networks

    Serial.println("Scanning available networks. May take some seconds.");

    Serial.println(scannerNetworks.readNetworks());

    // currently connected carrier

    Serial.print("Current carrier: ");

    Serial.println(scannerNetworks.getCurrentCarrier());

    // returns strength and ber

    // signal strength in 0-31 scale. 31 means power > 51dBm

    // BER is the Bit Error Rate. 0-7 scale. 99=not detectable

    Serial.print("Signal Strength: ");

    Serial.print(scannerNetworks.getSignalStrength());

    Serial.println(" [0-31]");

}
