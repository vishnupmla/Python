class Time:
    def __init__(self,hour,minute,second) -> None:
        self.__hr=hour
        self.__min=minute
        self.__sec=second

    def __add__(self,other):
        ttl_hr = self.__hr+other.__hr
        ttl_min = self.__min+other.__min
        ttl_sec = self.__sec+other.__sec
        if ttl_sec > 60:
            ttl_min = ttl_min+ttl_sec//60
            ttl_sec = ttl_sec%60
        if ttl_min > 60:
            ttl_hr = ttl_hr+ttl_min//60
            ttl_min = ttl_min%60
        print("Total time = {} hrs : {} min : {} sec".format(ttl_hr,ttl_min,ttl_sec))
            
    
t1= Time(3,23,45)
t2 = Time(5,56,57)

t1+t2