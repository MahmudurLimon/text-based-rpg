def moveable_object():
    edge=str('.')
    width = 50
    height = 10

    for i in range(height):
        if i == 0 or i == height - 1:  # First or last row
            print(edge * width)
        else:  # Middle rows
            print(edge + ' ' * (width - 2) + edge)
    #xedge=str(".")
    #xwidth=int(36)
    #xheigt=int(8)
    #for i in range(xwidth):
    #    print(xedge, end='')
    #for i in range(xheigt):
    #    print(xedge)
    #for i in range(xwidth):
    #    print(xedge, end='')
    #for i in range(xheigt):
    #    print(xedge)


moveable_object()