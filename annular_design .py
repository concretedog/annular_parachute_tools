"""
This program takes the desired diameter and number of gores for an annular parachute and gives you the dimensions needed to manufacture it.

"""
def annular():
    from math import pi

    try:
        Dd = float(input('Enter Desired Diameter: '))
        g = float(input('Enter Desired Number of Gores: '))

    except ValueError:
        print('Invalid Number')

    Dc= float(Dd*1.04) #Constructed Diameter
    Di= float(Dd* 0.94) #Inflated Diameter
    Vo= float(Dd*0.611) #Vent Opening Diameter
    Ml= float(Dd*1.25) #Main Line Length Edge lower skit to connection point
    Gh= float(Dd*0.304) #Gore Height
    Ga= float(Dd*0.209) #Gore Apex Inflated
    Vp= float(Dd*0.319) #Vent Pull Down Line Length
    Mi= float(Dd*0.2) #Main insert point (where pull down line joins main line)
    Gwt= float(pi*Vo/g) #Gore Width at top of vent
    Gwb= float(pi*Dc/g) #Gore width at bottom of skirt
    
    print('______________________________________')
    print ('The constructed diameter is',Dc)
    print ('The inflated diameter is',Di)
    print ('The vent hole diameter is', Vo)
    print ('The main line length (from base of skirt to connection point)',Ml)
    print ('The gore apex when inflates is', Ga)
    print ('The vent pull down line length is', Vp)
    print ('The main insert point where the vent pull down joins the main line is', Mi)
    print ('The gore width at the top - vent side', Gwt)
    print ('The gore width at the bottom - skirt side', Gwb)
    print ('The height of each gore is',Gh)
    print ('All dimensions do not include seam allowances')

if __name__ == '__main__':
    while True:
        annular()
        answer = input('Do you want to exit? (y) for yes ')
        if answer == 'y':
            break
