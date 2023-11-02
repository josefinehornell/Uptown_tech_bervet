import turtle

#Hej! Här har vi en sköldpadda som skapar en blå kvadrat.
#Ert uppdrag är att ändra på koden så att sköldpaddan istället skapar en gul stjärna!

t = turtle.Turtle()     #Denna funktionen skapar en sköldpadda
t.shape('turtle')       #Gör så att sköldpaddan ser ut som en sköldpadda
t.speed(1)              #1 = långsamt, 10 = snabbt,  0 = supersnabbt!
t.color('blue')         
t.begin_fill()          #Mellan begin_fill() och end_fill() fyller sköldpaddan in de former den ritar.
for x in range (4):     #En loop som pågår 4 gånger
    t.forward(100)      
    t.left(90)          #Man kan även gå höger med right()
t.end_fill()


input() #Man kan behöva klicka på play 2 ggr