% Convert annotations from matlab to json
a = jsonencode(annotations)
dlmwrite('test.txt',a,'delimiter','');

% Each entry in the map corresponds to the annotations of an image. 
% Each entry contains many cell tuples as annotated food
% A tuple is composed of 8 cells with the annotated:
% - (1) item category (food for all tuples)
% - (2) item class (e.g. pasta, patate, ...)
% - (3) item name
% - (4) boundary type (polygonal for all tuples)
% - (5) item's boundary points [x1,y1,x2,y2,...,xn,yn]
% - (6) item's bounding box [x1,y1,x2,y2,x3,y3,x4,y4]