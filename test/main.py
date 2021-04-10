from dearpygui.core import *            ## Dear PyGui Gui Library (Frontend)
from dearpygui.simple import *
from jpype import *                     ## Jpype um externe Java Funktionen zu verwenden
import builtins                         ## builtins um variablen in int zu konvertieren. -->
                                        ## Hat einen Bug gefixt der immer noch keinen Sinn macht

## Import Java Code
startJVM(getDefaultJVMPath(),"-ea", "-Djava.class.path=java/winkel_berechnung.jar")
mathe = JClass("com.nikita.gg.Main")

## Definiere globale variablen
vx = 0
vy = 0
ux = 0
uy = 0
shift = 340     ## shift value, Das Verschieben der Mitte des Koordinatensystems von DearPyGui,
                ## weil es sonst bei x = 0, y = 0 liegen würde




############################################################
##                                                        ##
##                  Definiere Funktionen                  ##
##                                                        ##
############################################################

## callback funktion zum Slider updaten
## (Wenn die slider verschoben werden, werden auf vx, vy, ux, uy neue werte gesetzt)

def update_drawing(sender, data):
    global vx, vy, ux, uy
    modify_draw_command("drawing##widget", "Vektor1", p1=[vx, vy])
    modify_draw_command("drawing##widget", "Vektor2", p1=[ux, uy])
    vx = get_value("Koordinaten von vx") + shift
    vy = get_value("Koordinaten von vy") + shift
    ux = get_value("Koordinaten von ux") + shift
    uy = get_value("Koordinaten von uy") + shift

## Berechnung der Winkel anhand von den in update_drawing gesetzten Werten
## und Erneuerung des ##Lösung## Textes

def berechnen(sender, data):
    vxr = builtins.int(vx - shift)
    vyr = builtins.int(vy - shift)
    uxr = builtins.int(ux - shift)
    uyr = builtins.int(uy - shift)
    mathe.winkel_zwischen_zwei_vektoren_2d(vxr, vyr, uxr, uyr, 20)
    lösung = str("Der Winkel zwischen Vektor V [" + str(vxr) + ", " + str(vyr) + "] und U [" + str(uxr) + ", " + str(uyr) + "] ist : " + str(int(mathe.winkel_zwischen_zwei_vektoren_2d(vxr, vyr, uxr, uyr, 0))) + "° !")
    set_value("##Lösung##", lösung)


############################################################
##                                                        ##
##                      Erstelle Fenster                  ##
##                                                        ##
############################################################

set_main_window_size(1450, 950)
set_global_font_scale(1.45)
set_theme("Gold")

with window ("MainWin"):

    with group("Drawing Controls Group"):
        add_slider_float("Koordinaten von vx", vertical=False, min_value=-280, max_value=280, callback=update_drawing)
        add_spacing(count=12)
        add_slider_float("Koordinaten von vy", vertical=False, min_value=-280, max_value=280, callback=update_drawing)
        add_spacing(count=12)
        add_slider_float("Koordinaten von ux", vertical=False, min_value=-280, max_value=280, callback=update_drawing)
        add_spacing(count=12)
        add_slider_float("Koordinaten von uy", vertical=False, min_value=-280, max_value=280, callback=update_drawing)

with window ("Vektor Graph", width=680, height=680):
    add_button("Berechnen", callback=berechnen)
    add_spacing(count=12)
    add_drawing("drawing##widget", width=1200, height=840)
    draw_circle("drawing##widget", [shift, shift],35 , [52, 235, 195] )
    draw_line("drawing##widget", [get_value("Koordinaten von vx"), get_value("Koordinaten von vy")], [shift, shift], [0, 200, 255], 2, tag="Vektor1")
    draw_line("drawing##widget", [get_value("Koordinaten von ux"), get_value("Koordinaten von uy")], [shift, shift], [235, 64, 52], 2, tag="Vektor2")
    set_window_pos("Vektor Graph", 15, 195)

with window ("Lösung", width=740, height=460):
    set_window_pos("Lösung", 710, 195)
    add_text("##Lösung##", parent="Lösung", color=[235, 64, 52], default_value="Lösungen hier!!")

## Starte DearPyGuii
start_dearpygui(primary_window="MainWin")


## Beende die Java Virtual Machine, die die Berechnungsfunktion geladen hat
shutdownJVM()

##   Methoden in com.nikita.gg.Main
## mathe.winkel_zwischen_zwei_vektoren_3d(vx, vy, vz, ux, uy, uz, resultvariable)
## mathe.winkel_zwischen_zwei_vektoren_2d(vx, vy, ux, uy, resultvariable)
