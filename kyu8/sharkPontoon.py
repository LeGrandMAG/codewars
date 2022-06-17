def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if (dolphin ==True):
        shark_speed = shark_speed/2
    mytime =  pontoon_distance/you_speed

    sharktime = shark_distance/shark_speed

    if sharktime <= mytime:
        return "Shark Bait!"
    else:
        return "Alive!"
    #pass # Don't get eaten!

shark(5,20,10,50,False)
    