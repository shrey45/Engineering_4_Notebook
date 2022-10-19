# Engineering_4_Notebook

&nbsp;

## Table of Contents
* [Launch Pad #1](#Launch_Pad_#1)
* [Onshape_Assignment_Template](#Onshape_Assignment_Template)

&nbsp;

## Launch Pad #1

### Assignment Description

This was a very simple introductory assignment - We had to get a countdown from 10 - 0 on the Terminal Window and print "LIFTOFF" at the end.

### Evidence 

Pictures / Gifs of your work should go here. You need to communicate what your thing does. 

### Wiring

Thankfully, there was no wiring

### Code
``` python

for i in range(10,0,-1):
#turn on & off led for .5 sec
    led.value = True
    time.sleep(.5)
    print(i)
    led.value = False
    time.sleep(.5)
#turn on green led at end
print('LIFTOFF')
led2.value = True

```
### Reflection

This was a really easy assignment and I had no troubles with it. All you have to do is insert a for() loop and set an interger to print from 10 to 0.

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link

[How to make a rocket](https://pbskids.org/)

### Test Image

![taco4life](images/download.jfif)

### Test GIF

![ayo](images/giphy.gif)
