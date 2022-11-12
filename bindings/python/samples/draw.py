# rgbmatrix drawing helpers
from rgbmatrix import graphics

def DrawRow(matrix, rowIndex, r=64, g=64, b=64):
    width = matrix.width
    for x in range(0, width):
        matrix.SetPixel(x, rowIndex, r, g, b)        
    
def DrawColumn(matrix, colIndex, r=64, g=64, b=64):
    height = matrix.height
    for y in range(0, height):
        matrix.SetPixel(colIndex, y, r, g, b)
        
def DrawRows(matrix, rows, r=64, g=64, b=64):
    """
    rows is a list of integers, defining the row indices to draw
    """
    for row in rows:
        DrawRow(matrix, row)

def DrawColumns(matrix, cols, r=64, g=64, b=64):
    """
    columns is a list of integers, defining the row indices to draw
    """
    for col in cols:
        DrawColumn(matrix, col)

def DrawPointsInWhite(matrix, pts, white=64):
    for pt in pts:
        matrix.SetPixel(pt[0], pt[1], white, white, white)

def DrawCirclesInWhite(matrix, pts, white=64, radius=5):
    for pt in pts:
        DrawCircle(matrix, pt[0], pt[1], radius, white, white, white)        

def DrawPoints(matrix, pts):
    """
    Draws a list of pts into matrix
    pts is a list of [x,y,r,g,b] list/tuples.
    """
    for pt in pts:
        matrix.SetPixel(pt[0], pt[1], pt[2], pt[3], pt[4])

def DrawCircle(matrix, x, y, radius, r, g, b):
    color = graphics.Color(r,g,b)
    graphics.DrawCircle(matrix, x, y, radius, color)

def DrawLine(matrix, x1, y1, x2, y2, r, g, b):
    color = graphics.Color(r,g,b)
    graphics.DrawLine(matrix, x1, y1, x2, y2, color)