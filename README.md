# Weather-project-IoT
IoT project with a DHT11 sensor
Pico-W-Stub that is created when you configure your project on pico is gitignored. 

Hello! my name is Kalle Andreasson (ka223ey). I have made a IoT project that sends the temperature and humidity to Adafruit from a Raspberry pico. The temperature and humidity is collected with a sensor called DHT11. I have also set a thresh hold on 25 degrees, If the temperature is above 25 degrees then I will also upload that to adafruit but in a different feed. If you are completely new to IoT this project might take a couple of weeks, this was my second project within IoT and it took me 3-4 weeks. 

I chose this project because I already had some of the hardware at home and the project seemed to be fairly simple and fun to do, so I thought it would be a good beginner project. The purpose of my project is to read the temperature and humidity then upload it to a cloud service called Adafruit were i visualize it with graphs. It's main purpose is to tell the temperature and humidity. I've learned more about Adafruit, how to connect the hardware on a raspberry pico w and also gained more knowledge when it comes to coding in micropython. 

| Hardware  | Link |
| ------------- | ------------- |
| For my raspberry i used the raspberry pi pico w, costs 84SEK  | [Raspberry pi pico w](https://www.electrokit.com/produkt/raspberry-pi-pico-w/) |
| Standard breadboard used to connect the hardware, costs 62SEK  | [Breadboard](https://www.electrokit.com/produkt/kopplingsdack-840-anslutningar/) |
| Basic jumper cabmles with male pins, costs 50SEK  | [Jumper cables](https://www.electrokit.com/produkt/labbsladd-40-pin-30cm-hane-hane/) |
| Pin strip, costs 10SEK  | [Pin strip](https://www.electrokit.com/produkt/stiftlist-2-54mm-1x40p-brytbar/) |
| DHT11 sensor used to meassure temperature and humidity, costs 63SEK  | [DHT11 sensor](https://www.amazon.se/gp/product/B089W8DB5P/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&th=1) |

The raspberry is the mind of the whole setup, it's a micro computer. The raspberry is where you write your code, my code is written in micro python. The breadboard is used to easier connect the hardware to each other with pin holes that you connect the jumper cables to. Pin strip is used to install the raspberry on the breadboard and last the sensor is used to meassure the temperature and humidity and is connected to the raspberry with jumper cables. 
