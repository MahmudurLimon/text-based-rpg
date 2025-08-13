def function():
    edge=str('.')
    center=str(' ')
    width=int(40)
    height=int(10)
    for i in range (height):
        if i==0 or i==height-1:
            print(edge*width)
        else:
            print(edge + center*(width-2) + edge)

function()