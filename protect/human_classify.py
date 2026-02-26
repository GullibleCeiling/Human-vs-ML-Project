def human_classify(culmen_depth_mm):
    if culmen_depth_mm < 17.0:
        return 'Gentoo'
    elif culmen_depth_mm > 19.0:
        return 'Adelie'
    else:
        return 'Chinstrap'
