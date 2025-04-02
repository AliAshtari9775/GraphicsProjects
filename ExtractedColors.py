import colorgram

image_path = 'E:\Python Programs\GraphicsProjects\GraphicsProjects\image.jpg'
number_of_colors = 20
colors = colorgram.extract(image_path, number_of_colors)
color_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_tuple = (r, g, b)
    color_list.append(color_tuple)

for color in color_list:
    print(color)
    if color[0]>=220 and color[1]>=220 and color[2]>=220:
        color_list.remove(color)

print(len(color_list))
for i in color_list:
    print(i)
# color_list = [(149, 75, 50),
#               (222, 201, 136),
#               (53, 93, 123),
#               (170, 154, 41),
#               (138, 31, 20),
#               (134, 163, 184),
#               (197, 92, 73),
#               (47, 121, 86),
#               (73, 43, 35),
#               (145, 178, 149),
#               (14, 98, 70),
#               (232, 176, 165),
#               (160, 142, 158),
#               (54, 45, 50),
#               (101, 75, 77),
#               (246, 242, 244),
#               (202, 164, 110),
#               (236, 239, 243),
#               (149, 75, 50),
#               (222, 201, 136),
#               (53, 93, 123),
#               (170, 154, 41),
#               (138, 31, 20),
#               (134, 163, 184),
#               (197, 92, 73),
#               (47, 121, 86),
#               (73, 43, 35),
#               (145, 178, 149),
#               (14, 98, 70),
#               (232, 176, 165),
#               (160, 142, 158),
#               (54, 45, 50),
#               (101, 75, 77),
#               ]
#
