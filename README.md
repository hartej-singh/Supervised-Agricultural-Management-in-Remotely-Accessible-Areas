--> Arduino Code - the GSM connection:
Libraries Included and their Functions:
GSM.h - used to connect to networks to send and receive messages from the Arduino to the Concerned Device.

Implementation Steps of the Arduino Code:
1. Import the GSM Library
2. Define the PINNumber of the network we connect to.
3. Initialise the Library Instance.Include a “true” parameter for debug enabled
4. Get the IMEI Number. Add some Error Messages for Error handling.
5. Under Void setup, Make the PinMode of Pin 8 to OUTPUT and Pin A0 to Input. Being the Serial connection at 9600 baud rate. Reset the Modem. Make the boolean variable and set the value to true, this tells us that the connection is not secured. Under the while loop, check if the GSM module is ready for connection, if it is , then connect and make the boolean values false. If not ready, add 1 sec delay and try again for connection. Get the modem parameters. Print the IMEI number and the Signal Strength
6. Under Void Loop, Make a loop to send and receive messages from the GSM module to the Arduino Board. Take the Input from the Sensors and check the humidity levels, If the humidity level at certain point of time is more than the threshold, turn on the dehumidifier. Print the Network Details.





--> The AI Model - Humidity and Temperature prediction:
Libraries Included and their functions:
Numpy - mathematical tools
Pandas - data management and analysis
Matplotlib - creating graphs and other visualizations
Sklearn - scaling of data features in a given range, generating predictive scores
Tensorflow Keras - for creating RNN and its implementation
JobLib - pipelining tool used save cache of configurations and use the smae in other programs

Implementation Steps of the AI model:
1. Import the necessary libraries. Import the dataset using pandas read csv files function. Generate the train dataset. Use the MinMaxScaler provided by sklearn to transform the train set. From the train set, make x_train and y_train. For RNN, x_train has to be a list of lists. Each list item will contain a list of previously decided number of days humidity values. Reshape the x_train using numpy functions based of the RNN input mechanism. 
2. Now, for making the RNN model, set the model type to be Sequential and add layers to it. 1 input layer and 3 hidden layers with all units equal to days. Add a dropout layer after each of the above mentioned 4 layers and add a dense layer of 1 unit which serves as the output layer. Compile the model with Adam optimizer, mean squared error loss and metrics as mae and mse. Fit the model with previously created x_train and y_train data and run for 100 epochs.
3. To test the mode, create a y_test list and reshape it using numpy functions based of the RNN input mechanism. Create x_test list by making an inputs list and transforming it using the MinMaxScaler. Then make x_test by making a list of previously decided number of days humidity values. Predict the values in y_pred using model.predict function used on x_test. Compare y_test and y_pred using R2 scores function defined by sklearn. A plot can be made of actual y values (y_test) and predicted y values (y_pred).
4. Save the model to .h5 format and also export the MinMaxScaler configuration to "scaler" file using the joblib module.





--> Mathematical Part Implementation:
Imnplementation Steps:
1.	The predicted humidity and temperature are taken as input.
2.	Calculate Saturation Vapour Pressure using the temperature.
3.	Calculate the humidity ration (x1) using the formula: 0.62198*RH*Pws/(P - RH*Pws). Where:
    a.	RH is the predicted relative humidity.
    b.	Pws is the calculated vapour pressure.
    c.	P is the standard pressure (101325 P).
4.	Similarly, calculate the humidity ratio for optimal humidity and temperature (50%, 25 °C).
5.	Calculate the air density for predicted temperature and humidity.
6.	Calculate Humidification Load using the formula: L*D*(X1-X2). Where:
    a.	L is the ventilation rate.
    b.	D is the calculated air density.
    c.	X1, X2 are the calculated humidity ratios.
7.	Calculate power consumed by multiplying load by 60 (Average power consumed by industrial humidifiers per kg/hour load).




--> Flask Code (Back-end of the Interface):
Libraries Included and their functions:
Numpy - mathematical tools
Pandas - data management and analysis
Matplotlib - creating graphs and other visualizations
Sklearn - scaling of data features in a given range, generating predictive scores
Tensorflow Keras - for creating RNN and its implementation
JobLib - pipelining tool used save cache of configurations and use the smae in other programs 

Implementation Steps of the Flask model:
1. Import the necessary libraries. Import saved model .h5 file and scaler files using joblib module. Import the dataset.
2. Patch the mathematical part code in this file.
3. Initialise the Flask app.
4. Make a default the route and give "POST" and "GET" methods. Under the POST method, receive the values from the front-end and give that as an input to the AI model. Use the preprocessing steps of the AI model. 
5. Send the predicted temperature value to the mathematical code patch. 
6. Send the required data to the front-end using the render_template function.
7. At the last, use app.run() to run the back-end code.



--> WebPage Code (Front-end of the Interface)
Implementation Steps:
1. Implement and include the necessary css scripts.
2. Include the javascript part used. 
3. Elements used:
    a. Heading 
    b. Body
    c. Table that fetches database entries for selected day.’
    d. Subform to get date input from the user
    e. Submit button to call the javascript code to process and give output 

