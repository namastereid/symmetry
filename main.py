import gizeh

# surface = gizeh.Surface(width=320, height=260) # in pixels
# circle = gizeh.circle(r=30, xy= [40,40], fill=(1,0,0))
# circle.draw(surface) # draw the circle on the surface
# surface.write_to_png("circle.png") # export the surface as a PNG

Pi = 3.14
# circ = gizeh.circle(r=30, xy=(50,50), fill=(1,1,1))
# rect = gizeh.rectangle(lx=60.3, ly=45, xy=(60,70), fill=(0,1,0), angle=Pi/8)
# sqr = gizeh.square(l=20, stroke=(1,1,1), stroke_width= 1.5)
# arc = gizeh.arc(r=20, a1=Pi/4, a2=3*Pi/4, fill=(1,1,1))
# text = gizeh.text("Hello world", fontfamily="Impact",  fontsize=40,
#                   fill=(1,1,1), xy=(100,100), angle=Pi/12)
# polygon = gizeh.regular_polygon(r=40, n=5, angle=Pi/4, xy=[40,50], fill=(1,0,1))
# line = gizeh.polyline(points=[(0,0), (20,30), (40,40), (0,10)], stroke_width=3,
#                      stroke=(1,0,0), fill=(0,1,0))

square_1 = gizeh.square(l=20, xy = [30,35], fill=(1,0,0))
square_2 = square_1.rotate(Pi/8) # rotation around [0,0] by default
square_3 = square_2.rotate(Pi/4, center=[10,15]) # rotation around a center
square_4 = square_1.scale(2) # two times bigger
square_5 = square_1.scale(sx=2, sy=3) # width times 2, height times 3
square_6 = square_1.scale(2, center=[30,30]) # zoom: scales around a center
square_7 = square_1.translate(xy=[5,15]) # translation

square = gizeh.square(l=20, fill=(1,0,0), xy=(40,40))
circle = gizeh.circle(r=20, fill=(1,2,0), xy=(50,30))
group = gizeh.Group([square, circle])
group_1 = gizeh.Group([square, circle])
group_2 = group.translate(xy=[30,30]).rotate(Pi/4)
group_3 = gizeh.Group([circle, group_1])

surface = gizeh.Surface(width=300,height=200)
group.draw(surface)
group_1.draw(surface)
group_2.draw(surface)
group_3.draw(surface)
surface.write_to_png("my_masterwork.png")