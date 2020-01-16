# CircuitPython
   My CircuitPython Assignments. 
   These are my CircuitPython assignments from Engineering 3
 
 
 
 
 
 
 
 
 
 ## Hello Circuit Python (and Metro and Mu)
 
 ### Description
 In this assignment, we are introduced to CircuitPython, Metro, and Mu. The objective is to make an LED fade from 0% to 100% brightness and back down.
 
 ### Lessons Learned
  This assignment was essentailly and introduction to Metro, CircuitPython, and Mu. I learned that the logic for your code will be nearly identical for an LED Fade across languages, but the syntax can be wildly different; as in the contrast between Arduino and CircutPython. Also, I learned that CircuitPython requires much more libraries to be imported than Arudino
  
 ### Images and Diagrams
 This is a Fritzing of the Wiring

<img src="MyMedia/LED_Fade_Fritzing_bb.png" width="512">
   
 
 
 
 
 
 ## CircuitPython Servo (With Capacitive Touch)
 ### Description
 In this assignment, we used CircuitPythons's "Capacitive Touch" to make a Servo turn. When we touch a wire, then the servo will rotate a certain direction. If we were to touch another wire, then the Servo would rotate the other direction.
 ### Lessons Learned
 This lesson, we learned how to use PWM, as well as re-familiarizing ourselves with how CircuitPython Works. Capacitive touch was relatively easy to become accustomed to (Touch.io)
 ### Images and Diagrams
  This is a Fritzing diagram of the assignment
  
  <img src="MyMedia/Servo_bb.png" width="512">
  
  
  
  
  
  
  ## CircuitPython LCD
  ### Description
   In this assignment, we had to print a button press on an LCD screen. On top of that, we had to add or subtract the number per press based on if a switch on the breadboard was flipped or not. On flip of the switch would count up when the button was pressed, and the otehr would count down when the button was pressed
   
   ### Lessons Learned
   In this assignment, we re-familiarized ourselves with how to wire a switch, as well as a LCD Sceren. Fortunately for us, the Metro Express has two LCD Backpack friendly ports for SDA and SCL. This means that we did not have to set any Analog Pins for the LCD Backpack
   
   ### Images and Diagrams
   
   
   
   <img src="MyMedia/LCDWiring.png" width="512">
   
   
   
   
   ## CircuitPython PhotoInterrupters
  
 ### Description
In this assignment, we had to read interrupts in a photointerrupter, and print the ammount of interrupts every 4 seconds, WITHOUT using time.sleep().
   
 ### Lessons Learned
 I learned about time.monotonic in this assignment and used it to count the amount of seconds (intervals). We also added a switch that only adds once the photointeruppter reading is high then low, essentially functioning as a safeguard for the counter.
   
 ### Images and Diagrams
 
 <img src="MyMedia/Photointerrupter%20assignment.png" width="512">
   





 ## CircuitPython Distance Sensor
 
  ### Description
In this assignment, we had to read the distance from an UltraSonic Distance Sensor (HC-SR04). After we had read the distance, we were to turn the onboard NEOPIXEL LED along a spectrum to a color that represents the distance. The distance is to also be printed to the Serial Monitor.
   
 ### Lessons Learned
This assignment taught me quite a deal about raw problem solving and Critical Thinking. The distance sensor itself was rather easy and straightforward; however, the color spectrum was the more difficult part of the project. I solved the problem by spending some time and thinking about what i want the colors to be at what distance, and how that could be mapped. I ended up using two different mapping regions as you had to bypass the halfway (15cm) distance.

   
 ### Images and Diagrams
 
  <img src="MyMedia/Distance_Sensor.png" width="512">

 
 
 
 
 
 ## Classes, Objects, and Modules
 
 ### Description
 In this assignment, we leared about Classes, Objects, and Modules in CircuitPython. In the assignment itself, we had to create a library that would set an LED to a certain color when the main called for it. You fed the main certain pins, and the LED would turn itself through colors, and at the end it would fade in and out like a rainbow.
 
 ### Lessons Learned
 In this, we were introduced to Classes, Objects, and Modules. It took quite a bit of effort to get the syntax of the library correct. Eventually, we were able to decude how it was done. We also had to use PWM pins and self in order for the LEDs to turn on. The most frustrating issue was the learning curve for Self. Self must be added in your library in order to allow initialized variables to be accessed and referenced later in your library. 
 
 ### Images and Diagrams



<img src="MyMedia/Untitled%20Sketch%202_bb.png" width="512">




## Hello VS Code

### Description
   In this assignment, we were introduced to Visual Studio (VS) Code. We opened VS code, created a small file, and pused that file into our CircuitPython Github Repository.  
   
  ### Lessons Learned
  Although this assignment is very straightforward on the surface level, it was actually rather difficult. VS Code does take a decent amount of familiarization in order to make sense. On top of that, I was given errors that didn't seem to have much reasoning. Eventually, I was able to work through the errors. Makes sure that your Metro is plugged in and that you have installed Python
  
 ## FancyLED
 
 ### Description
 
 In FancyLED, we had to create a library in FancyLED that had various modules that each made a set of 6 LEDs do different tasks. For example, there was a blink (all on or all off) module and a chase (one on, then off, then the next on while the intial was being turned off) module.
 
 ### Lessons Learned
 The biggest lesson I learned from this assignment was that it can be, and is likely usally, beneficial to look back at prior asssignments and work for help on your current work. More specifically, it behooved me to look at the RGB library from the "Classes, Modules, and Objects" assignment. 
 
 ### Images and Diagrams
 
 MyMedia/FancyLED_bb.png
 
 <img src="MyMedia/FancyLED_bb.png" width="512">
 
 
 # Advanced Circuit Python
 
 ## Hello Processing
 
 

### Description
   In this assignment we were supposed to make a circle bounce around a small window.
   
 ### Lessons Learned
  In this assignment, I learned that planning your code instead of just wriitng it and troubleshooting can really help. At first, I just attempted it blindy and thought I would just figure it out. However, that did not work very well... at all. So, I took a step back from my keyboard, and really thought through the code and what lines I needed. It was very easy to transpose my new information on to the keyboard.
  
 ### Images and Diagrams
 
 

