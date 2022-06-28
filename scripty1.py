class forever():
    def hp_stat(base, iv, ev, level):
        bye = (((2*base+iv+(ev/4))*level)/100)+level+10
        if bye > 510:
            bye = 510

        else:
            bye = bye

        happy = bye
        return happy
            


    def other_stat(nat, bp, vi, ve, lev):
        return ((((2*bp+vi+(ve/4))*lev)/100)+5)*nat
