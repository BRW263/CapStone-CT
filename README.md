# CapStone-CT
Custom Tumblers CapStone for PDX Code Guild

# Custome Tumblers

## Overview
Building a Web App for users to buy pre-designed Tumblers and/or Design their own Custom Tumblers. The user will have the ability to choose from diffrent size tumblers, (8oz, 16oz, 20oz and 32oz) backgrounds(Plain, wood, marble,granite, ect...) effects(Peek-a-boo, crackle, fade, faze, ect...) and images or silhouette's that they can either choose from or upload themselves.

## Functionality
1. Main Page: User can view previously made Tumblers (most likley using a Carousel). With a navigational bar at the top

2. Views: I will have diffrent Views accessed from a drop down menu.

 1 will go to the Pre-Made section where the user can select from stock designs with images of all sides of each tumbler, with pricing, and an advisment stating that final product might slightly differ from the image(as to no two hand made tumblers are the exact same). 

 2 another view will go to the customazation are where the user will be able to select background, images, effects) and see what it will look like all together. Again with a notice that design might slightly differ from what is shown.
 
 3 The next view will be a shoping cart/checkout view where the user can choose between PayPal, Cash App, Venmo, ect... 

 4 This will be the about page. 

 5 will be the Contact page.

## Process to Completion
User (built into django)
TumberSize
    name (charfield)
    image (imagefield)

TumblerBackground
    name (charfield)
    image (imagefield)

TumblerEffect
    name (charfield)
    image (imagefield)

TumblerOrder
    user (foreignkey to user)
    size (foreignkey to tumblersize)
    background (foreignkey to tumblerbackground)
    effect (foreignkey to tumblereffect)
    image (imagefield)

PremadeTumblerOrder
    name
    image1
    image2
    image3
    
PremadeTumblerOrderImage
    PremadeTumblerOrder (foreign key)

 ## Time line.
 Week 1.
   research payment systems?
   user management system
   make models, enter size/background/effect data

    
 Week 2.
   allow users to enter a order
   style?
   pre-made tumbler order?

 Week 3.
   more style?
   better payment processing
