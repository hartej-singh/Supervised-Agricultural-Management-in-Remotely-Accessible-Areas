# Abstract
Humidity can adversely affect the growth of plants. When conditions are too humid, it may promote the growth of mould and bacteria that cause plants to die and crops to fail, as well as conditions like root or crown rot. Humid conditions also invite the presence of pests, such as fungus gnats, whose larvae feed on plant roots and thrive in moist soil. The need of maintaining humidity levels in the plantation area is a must, especially in remote areas that have no electricity.
Water is an essential part in agriculture as it processes germination of seeds, growth of plant roots, nutrition, multiplication of soil organisms and other hydraulic processes in the plant. Water is also present in the atmosphere in the form of humidity and it is also essential for proper growth of plants but excessive humidity can lead to an increasing amount of transpiration water loss.


# Introduction
•	Humidity can adversely affect the growth of plants.

•	The need of maintaining humidity levels in the plantation area is a must, especially in remote areas that have no electricity.

•	The required electricity for such areas is generated through fuel-operated electricity generators.

•	Sensors are deployed at the area to detect various parameters.

•	These sensors are connected to an Arduino board which converts the analog data to readable data with which it controls and corrects the parameters instantaneously to the pre-specified range.

•	Arduino board also digitizes the data and publishes it to the Cloud using a GSM module for analysis and prediction.


# Problem Statement
Our project involves plantation in remote areas where there is no electricity supply available. The required electricity is generated through fuel-operated electricity generators. Sensors are deployed at the area to detect various parameters. These sensors are connected to an Arduino board which converts the analog data to readable data with which it controls and corrects the parameters instantaneously to the pre-specified range. Along with that, the Arduino board digitizes the data and publishes it to the Cloud using a GSM module. The data is received at the monitoring station where the fuel requirement for the next term is predicted using Artificial Intelligence techniques. This will enable the people to prepare in advance about when to visit the remote area to refuel the electricity generators.
Each IoT device collected a total of seven different readings from the four sensors on a regular interval. Sensor readings include temperature, humidity, carbon monoxide (CO), liquid petroleum gas (LPG), smoke, light, and motion. In our project, we predict humidity levels at the monitoring stations as artificial humidity controller i.e., dehumidifiers are installed which run on electricity (from generators running on fuel).
Software Implementation:
•	Arduino IDE and sensor-specific libraries
•	Tensorflow/Keras for AI model (RNN-based)
•	AWS Cloud for data collection, display, and storing purpose


# Literature Review
The progress in the innovation invention of agriculture field has been developed into most challenging task especially because of increasing demand on the standard of agricultural projects and human unavailability in rural agricultural areas. The existing works are on the rural area agricultural plots, by maintaining water and energy to provide the crop to be grown. Whereas, as the crop grows in these areas, it lacks the frequent sprays with water, when a farmer anticipates dry weather ahead. This human intervention cannot be replicated by just using mere robotic actuators and solar panels. Our Project reaches this humidity level maintenance, without human intervention, by maintaining dehumidifiers. We still have the energy generators that require occasional refuelling, this can be achieved by taking in the external factors as the temperature and humidity and send it to the cloud server database, where our project has a machine learning model based on recurrent neural networks to predict the humidity and temperature of the next day based on the trend of the last 30 days preceding it. Ultimately, the predicted values can determine the energy used on a particular day and thus we can plan a visit to the agricultural site for refuelling. Apart from refuelling, we also have Arduino controlled sensors and actuators that work on the field for purely agricultural activities. Mathematical calculations were based on the psychometric chart, chart use the provided details such as Relative humidity, enthalpy, dry bulb temperatures and pressure to calculate the humidity ratio. These values of the humidity values are then used to find us the humidification load.


# Methodology
In our prototype with the use of 3 sensory devices, we collect necessary data relating to agricultural environment that affects humidity level situated in a remote area. This data is sent to Arduino which does the instantaneous detection, control and correction of the environment. We also use the GSM module embedded in Arduino to transmit the data over Cloud to the end-user which makes use of Deep Learning techniques to predict future fuel requirements for the on-site electricity generator to operate the humidity controller.


# Proposed Solution
•	We collect necessary data relating to agricultural environment that affects humidity level situated in a remote area with the use of 3 sensory devices.

•	This data is sent to Arduino which does the instantaneous detection, control and correction of the environment.

•	GSM module is embedded in Arduino to transmit the data over Cloud to the end-user.

•	The end user uses Deep Learning techniques to predict future fuel requirements for the on-site electricity generator to operate the humidity controller.

•	The Arduino is attached with actuators to work on site, based on the values the sensors give. The watering actuators works on this basis.

•	The water level sensors are used to detect the water present in the tank and therefore turn on the water pump if the water level is below the threshold.

 
 
# Experimental Details:
## Dataset details:
•	Data is collected from a series of custom-built environmental sensor arrays. Each breadboard-based sensor array is connected to a Arduino board, which are placed in physical locations varied in temperature, humidity, and other environmental conditions.

•	Non-Copyrighted, public dataset collected from actual IOT devices.

•	The sensor readings, along with a unique device ID and timestamp, were published as a single message, using the ISO standard Message Queuing Telemetry Transport (MQTT) network protocol. 

•	The Entries consist of temperature, humidity, LPG levels, carbon monoxide levels, smoke levels, light detection and motion detection. 

•	Created on 20th July 2020 on kaggle.com

•	https://www.kaggle.com/garystafford/environmental-sensor-data-132k


## Arduino code:
The Arduino is used for many functions, we have 2 sensors connected to it, humidity sensor and water depth sensor. The Two sensors are connected to the analog pins and give the values to the Arduino. The dehumidifier and the watering actuator is connected to the digital pins of the Arduino. If the humidity sensor senses the humidity raising over the threshold, it turns on the dehumidifier for 5 minutes and then turns it off. If the water depth sensors read the value less than the min depth, the Arduino board turns on the water pump to fill the water tank. Every 3 hrs the plants are watered with 50 ml of water through the actuators. The GSM library is imported and utilizing the inbuilt functions, we initialize the GSM module and connect to a network. We keep the values of the network we are connected to the and the signal strength on a check.

## AI model:
AI model is based on a Deep Learning concept of Recurrent Neural Network. For prediction of future humidity values, we take in all the values of humidity for the previous moth (30 days), input them to the RNN mode, which gives the output as the humidity value of the 31st day. Similarly, for temperature, we follow the exact procedure. 

## Mathematical part:
•	To determine the humidification load required to make the relative humidity optimal for plant growth, we will use the psychrometric chart and the mathematical formula L=V*R*(X1-X2).
    o	Here, L is the humidification load that should be added to the airflow every hour.
    o	V is the ventilation rate.
    o	R represents the air density and (X1-X2) is the difference between the desired humidity levels. We need the psychrometric chart to determine the values of X1 and X2.

•	The ideal relative humidity for tropical plants if 50%.

•	Once we calculate L, we calculate the power consumed by the humidifier by multiplying by 60W, which is the average power consumed by industrial humidifiers for 1kg/hour of load

•	The psychrometric chart shows the dry-bulb temperature (DBT), the absolute humidity, the relative humidity, and the enthalpy at a standard pressure: 101325 Pa.

•	If we want to change the current humidity (30%, 20° C) to 50%, we first find the point of intersection of the 30% RH curve and the 20° C line (Point A).

•	Then we follow up the green enthalpy line to reach the 50% RH curve (Point B).

•	The intercepts of Point A and Point B on the y-axis are the values of X1 and X2 respectively. 

 

# Conclusion:
We successfully predict the power consumption of the humidifiers and plan the future refuelling trips. Thus, the remotely accessible agricultural area can be managed with ease. With an accuracy of about 80% and an interface with suggestive alert messages, we are able to determine how often we need to visit the area to refuel. The interface is also used to monitor the instantaneous sensor data report. On-site Arduino controlled actuators work on the field for the crops to be grown with healthy products. Hence, we completed all the objectives and conclude our project.

 
# Uniqueness:
•	Most of the papers available at this moment suggest the use of detectors but not predictors. Sensors are deployed in areas and when they detect any parameter which is not in range, they enable counter-measures to remediate it. 
•	Our project not only achieves this, but will also enable people to plan their fuel consumption. Moreover, for remote-locations, making frequent trips to refuel the electricity generators is not very feasible, so users will be able to schedule their visits more efficiently.
