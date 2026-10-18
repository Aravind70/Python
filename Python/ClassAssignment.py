class MultiFunction:
    def Subfields():
        print("Machine Learning \nNeural Network \nVision \nRobotics \nSpeech Processing \nNatural Language Processing")
        
    def OddEven(num):
        if(num%2 == 0):
            res = f"{num} is Even number"
        else:
            res = f"{num} is Odd number"
        return res
        
    def Eligible(gender, age):
    
        if(gender == "Male"):
            marriage_age = 24
        else:
            marriage_age = 21

        if(age >= marriage_age):
            out = "ELIGIBLE"
        else:
            out = "NOT ELIGIBLE"
        return out
        
    def Percentage(tot,numOfsubs):
        avg = tot/numOfsubs
        return avg
        
    def Area_of_triangle(Ht,Br):
        res = (Ht*Br) / 2
        return res
    def Perimeter_of_triangle(Ht1,Ht2,Br):
        res = Ht1+Ht2+Br
        return res