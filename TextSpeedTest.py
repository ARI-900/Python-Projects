from time import *
import random as r

def mistake(ranstr,userstr):
    error = 0
    for i in range(len(ranstr)):
        try:
            if (ranstr[i] != userstr[i]):
                error += 1
            else:
                continue
        except:
            error +=1
    return error

def speed(start,end,str):
    time_delay = end-start
    time_R = round(time_delay,3)
    speed = len(str)/time_R
    return round(speed)

if __name__ == '__main__':
    TextItem = ["The curious cat chased a fluttering butterfly through the lush garden.",
                "After a long day at work, she enjoyed a soothing bath filled with fragrant lavender bubbles.",
                "The old oak tree stood sentinel in the middle of the meadow, its branches reaching for the sky.",
                "As the sun dipped below the horizon, the city's skyline became a silhouette against the evening sky.",
                "The scientist meticulously recorded the data from the experiment, hoping for a groundbreaking discovery.",
                "The curious cat chased its own tail in endless circles, much to the amusement of onlookers.",
                "As the sun dipped below the horizon, the sky painted itself in vibrant shades of orange and pink.",
                "In the bustling city, a street musician played a soulful melody on his saxophone, captivating the passersby.",
                "The old bookshop on the corner was a hidden gem, filled with dusty tomes and forgotten stories waiting to be rediscovered.",
                "Lost in thought, she absentmindedly walked through the park, breathing in the crisp autumn air."]

    # generate random string
    ranStr = r.choice(TextItem)
    print(ranStr)
    start = time()
    print("")
    str = input("Enter: ")
    end = time()

    # err = mistake(ranStr,str)

    print("Speed: ",speed(start,end,str),"w/s")
    print(f"Errors: ",mistake(ranStr,str))