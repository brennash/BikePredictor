BikePredictor
=============

Predicting the Availability of Bikes across Dublin. There's a few ways of 
cracking this particular nut, build up large volumes of data and do an 
in-depth seasonal analysis, build up some data and use a more flexible model 
or just use the most recent data and trends be-damned!

This approach uses an auto-regressive integrated moving average (ARIMA) model
to plot ahead based on the volatility of the bike availabilities at the various 
bike stations. 
