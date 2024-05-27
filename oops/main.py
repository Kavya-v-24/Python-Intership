from vehicle import Bike,Car,Scooty,Bus,Auto
def main():
    bike=Bike("red", 2, 5)
    car=Car("black",4,5)
    scooty=Scooty("blue",2,0)
    bus=Bus("green",4,4)
    auto=Auto("yellow",3,0)

    bike.display_details()
    print("\n")
    car.display_details()
    print("\n")
    scooty.display_details()
    print("\n")
    bus.display_details()
    print("\n")
    auto.display_details()
    print("\n")

if __name__=="__main__":
    main()