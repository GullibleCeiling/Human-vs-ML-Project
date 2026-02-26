***

***




def human_classify(culmen_depth_mm): #This is the start of the function, classifying culmen depth
    if culmen_depth_mm < 17.0: #This checks if culmen length is under 17 mm
        return 'Gentoo' #if it is, it returns the species Gentoo
    elif culmen_depth_mm > 19.0: #However, 
        return 'Adelie'
    else:
        return 'Chinstrap'