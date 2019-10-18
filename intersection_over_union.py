
import numpy as np
import shapely
from shapely.geometry import Polygon, MultiPoint

polygon_coordinate_1 = [376, 116, 422, 116, 422, 130, 376, 130]  #four points coordinate
a = np.array(polygon_coordinate_1).reshape(4, 2)
area_poly1 = Polygon(a).convex_hull #area of polygon


polygon_coordinate_2 = [377, 117, 463, 117, 465, 130, 378, 130] #four points coordinate
b = np.array(polygon_coordinate_2).reshape(4, 2)
area_poly2 = Polygon(b).convex_hull #area of polygon

union_poly = np.concatenate((a, b))
# print(union_poly)
print(MultiPoint(union_poly).convex_hull)
if not area_poly1.intersects(area_poly2):
    iou = 0
else:
    try:
        inter_area = area_poly1.intersection(area_poly2).area
        # print(inter_area)
        union_area = MultiPoint(union_poly).convex_hull.area
        # print(union_area)
        if union_area == 0:
            iou = 0
        iou = float(inter_area) / union_area
    except shapely.geos.TopologicalError:
        iou = 0
print(iou)

