class owow():
    def dabest(bv, val, ort, level4):
        db = ((2*bv+val+(ort/4))*(level4/100))
        if db > 510:
            d1 = 510
        else:
            d1 = db
        return d1

    def ev_yarn(stat, modf, d1, level4):
        ev_total = ((((stat/modf)-(d1))*400/level4)/4)*4
        return ev_total 
