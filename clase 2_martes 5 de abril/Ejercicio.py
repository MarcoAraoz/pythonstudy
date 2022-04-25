from dataclasses import replace
from turtle import title


text = "IT was a special pleasure to see things eaten, to see things blackened and changed. With the brass nozzle in his fists, with this great python spitting its venomous kerosene upon the world, the blood pounded in his head, and his hands were the hands of some amazing conductor playing all the symphonies of blazing and burning to bring down the tatters and charcoal ruins of history. - FAHRENHEIT 451"
def parse_string(text):
    # minus = text.lower()
    # spl = minus.split(" ")
    # spl[0] = spl[0].title()
    # spl[-2] = spl[-2].capitalize()
    # correction = " ".join(spl)
    # return correction
    
    title = text.capitalize()
    title2 = title.replace("fahrenheit","Fahrenheit")
    print(title2)
    
parse_string(text)


#   minus = text.lower()
#   slc = minus.split(" ")
#   print(slc)
#   slc[0] = slc[0].capitalize()
#   slc[-2] = slc[-2].capitalize()
#   res = " ".join(slc)