from Focus_Roots import *



def change():

    draw_rect(100,100,300,300,0,color=color_brown)#hair

    draw_rect(150,100,200,200,0,color=color_skin)#skin

    draw_rect(170,160,50,30,0,color=color_white)#left eye
    draw_rect(280,160,50,30,0,color=color_white)#right eye

    draw_rect(188,160,15,30,0,color=color_sky_blue)#left eye
    draw_rect(298,160,15,30,0,color=color_sky_blue)#left eye

    draw_rect(200,250,100,30,0,color = color_white)

    draw_line([230,200],[230,220],color = color_black) 
    draw_line([230,220],[270,220],color = color_black) #nose
    draw_line([270,200],[270,220],color = color_black)

    draw_rect(230,300,50,50,0,color=color_skin)#hands

    draw_rect(150,350,30,200,0,color=color_skin)#hands
    draw_rect(330,350,30,200,0,color=color_skin)#hands

    draw_rect(190,350,130,170,0,color=color_aqua)
    draw_rect(140,350,50,50,0,color=color_aqua)#Dress
    draw_rect(320,350,50,50,0,color=color_aqua)

    draw_rect(150,100,30,50,0,color=color_brown)
    draw_rect(150,100,200,20,0,color=color_brown)#Hair
    draw_rect(320,100,30,50,0,color=color_brown)

draw(change)