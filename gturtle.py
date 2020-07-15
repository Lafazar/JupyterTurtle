# Version 0.1
from IPython.core.display import HTML
from IPython.core.display import Javascript
import time
import math

class Turtle:
    canvasNumber = 0
    width = 600
    height = 600
    x = width/2
    y = height/2
    direction = 270
    delay = 0.1
    lineWidth = 1
    strokeStyle = "blue"
    fillStyle = "cyan" #"#00000000" transparent (alpha channel 0)
    
    def __init__(self,newCanvasNumber):
        self.canvasNumber = newCanvasNumber

turtle = Turtle(0)
        
def home():
    global turtle
    turtle.x = turtle.width/2
    turtle.y = turtle.height/2
    turtle.direction = 270
    javaScriptCode = '\n'.join((
        'var cnv = document.getElementById("drawCanvas' + str(turtle.canvasNumber) + '");',
        'var ctx = cnv.getContext("2d");',
        'ctx.moveTo(' + str(turtle.x) + ', ' + str(turtle.y) + ');'
    ))
    display(Javascript(javaScriptCode))
    
def makeTurtle():
    global turtle
    previousCanvasNumber = turtle.canvasNumber
    newCanvasNumber = previousCanvasNumber+1
    turtle = Turtle(newCanvasNumber)
    htmlCode = '<canvas id="drawCanvas' + str(turtle.canvasNumber) + '" width="' + str(turtle.width) + '" height="' + str(turtle.height) + '"></canvas>'
    display(HTML(htmlCode))
    javaScriptCode = '\n'.join((
        'var cnv = document.getElementById("drawCanvas' + str(turtle.canvasNumber) + '");',
        'var ctx = cnv.getContext("2d");',
        'ctx.lineWidth = ' + str(turtle.lineWidth) + ';',
        'ctx.strokeStyle = "' + turtle.strokeStyle + '";',
        'ctx.fillStyle = "' + turtle.fillStyle + '";',
    ))
    display(Javascript(javaScriptCode))
    home()

def forward(distance):
    global turtle
    newX = turtle.x+distance*math.cos(turtle.direction/180*math.pi)
    newY = turtle.y+distance*math.sin(turtle.direction/180*math.pi)
    javaScriptCode = '\n'.join((
        'var c = document.getElementById("drawCanvas' + str(turtle.canvasNumber) + '");',
        'var ctx = c.getContext("2d");',
        'ctx.lineTo(' + str(newX) + ', ' + str(newY) + ');',
        'ctx.stroke();'
    ))
    display(Javascript(javaScriptCode))
    turtle.x = newX
    turtle.y = newY
    time.sleep(turtle.delay)
    
def back(distance):
    forward(-distance)

def right(angle):
    global turtle
    turtle.direction = (turtle.direction+angle)%360

def left(angle):
    right(-angle)

def dot(diameter):
    javaScriptCode = '\n'.join((
        'var cnv = document.getElementById("drawCanvas' + str(turtle.canvasNumber) + '");',
        'var ctx = cnv.getContext("2d");',
        'ctx.beginPath();'
        'ctx.arc(' + str(turtle.x) +', ' + str(turtle.y) +', ' + str(diameter/2) +', 0, 2 * Math.PI, false);'
        'ctx.fill();'
        'ctx.stroke();'
        'ctx.moveTo(' + str(turtle.x) + ', ' + str(turtle.y) + ');',
    ))
    display(Javascript(javaScriptCode))
    time.sleep(turtle.delay)

def leftArc(radius, angle):
    centerX = turtle.x+radius*math.cos((turtle.direction-90)/180*math.pi)
    centerY = turtle.y+radius*math.sin((turtle.direction-90)/180*math.pi)
    javaScriptCode = '\n'.join((
        'var cnv = document.getElementById("drawCanvas' + str(turtle.canvasNumber) + '");',
        'var ctx = cnv.getContext("2d");',
        'ctx.arc(' + str(centerX) +', ' + str(centerY) +', ' + str(radius) +', ' + str(turtle.direction+90) + ' / 360 * 2 * Math.PI, ' + str(turtle.direction+90-angle) + ' / 360 * 2 * Math.PI, true);'
        'ctx.stroke();'
    ))
    display(Javascript(javaScriptCode))
    turtle.direction = (turtle.direction-angle)%360
    newX = centerX+radius*math.cos((turtle.direction+90)/180*math.pi)
    newY = centerY+radius*math.sin((turtle.direction+90)/180*math.pi)
    turtle.x = newX
    turtle.y = newY
    time.sleep(turtle.delay)

def rightArc(radius, angle):
    centerX = turtle.x+radius*math.cos((turtle.direction+90)/180*math.pi)
    centerY = turtle.y+radius*math.sin((turtle.direction+90)/180*math.pi)
    javaScriptCode = '\n'.join((
        'var cnv = document.getElementById("drawCanvas' + str(turtle.canvasNumber) + '");',
        'var ctx = cnv.getContext("2d");',
        'ctx.arc(' + str(centerX) +', ' + str(centerY) +', ' + str(radius) +', ' + str(turtle.direction-90) + ' / 360 * 2 * Math.PI, ' + str(turtle.direction-90+angle) + ' / 360 * 2 * Math.PI, false);'
        'ctx.stroke();'
    ))
    display(Javascript(javaScriptCode))
    turtle.direction = (turtle.direction+angle)%360
    newX = centerX+radius*math.cos((turtle.direction-90)/180*math.pi)
    newY = centerY+radius*math.sin((turtle.direction-90)/180*math.pi)
    turtle.x = newX
    turtle.y = newY
    time.sleep(turtle.delay)
    
def setPos(x,y):
    global turtle
    turtle.x = x+turtle.width/2
    turtle.y = -y+turtle.height/2
    javaScriptCode = '\n'.join((
        'var cnv = document.getElementById("drawCanvas' + str(turtle.canvasNumber) + '");',
        'var ctx = cnv.getContext("2d");',
        'ctx.moveTo(' + str(turtle.x) + ', ' + str(turtle.y) + ');'
    ))
    display(Javascript(javaScriptCode))

def setColor(strokeStyle):
    pass

def setPenColor(strokeStyle):
    global turtle
    turtle.strokeStyle = strokeStyle
    javaScriptCode = '\n'.join((
        'var cnv = document.getElementById("drawCanvas' + str(turtle.canvasNumber) + '");',
        'var ctx = cnv.getContext("2d");',
        'ctx.beginPath();'
        'ctx.strokeStyle = "' + turtle.strokeStyle + '";',
        'ctx.moveTo(' + str(turtle.x) + ', ' + str(turtle.y) + ');'
    ))
    display(Javascript(javaScriptCode))

def setFillColor(fillStyle):
    global turtle
    turtle.fillStyle = fillStyle
    javaScriptCode = '\n'.join((
        'var cnv = document.getElementById("drawCanvas' + str(turtle.canvasNumber) + '");',
        'var ctx = cnv.getContext("2d");',
        'ctx.fillStyle = "' + turtle.fillStyle + '";',
    ))
    display(Javascript(javaScriptCode))

def setPenWidth(lineWidth):
    global turtle
    turtle.lineWidth = lineWidth
    javaScriptCode = '\n'.join((
        'var cnv = document.getElementById("drawCanvas' + str(turtle.canvasNumber) + '");',
        'var ctx = cnv.getContext("2d");',
        'ctx.beginPath();'
        'ctx.lineWidth = ' + str(turtle.lineWidth) + ';',
    ))
    display(Javascript(javaScriptCode))

def hideTurtle():
    pass

#source: https://codepen.io/Geeyoam/pen/vLGZzG
JavaScriptFloodFillCode = '''var canvas = document.getElementById("drawCanvas");
var ctx = canvas.getContext("2d");

function getColorAtPixel(imageData, x, y) {
  const {width, data} = imageData

  return {
    r: data[4 * (width * y + x) + 0],
    g: data[4 * (width * y + x) + 1],
    b: data[4 * (width * y + x) + 2],
    a: data[4 * (width * y + x) + 3]
  }
}

function setColorAtPixel(imageData, color, x, y) {
  const {width, data} = imageData

  data[4 * (width * y + x) + 0] = color.r & 0xff
  data[4 * (width * y + x) + 1] = color.g & 0xff
  data[4 * (width * y + x) + 2] = color.b & 0xff
  data[4 * (width * y + x) + 3] = color.a & 0xff
}

function colorMatch(a, b) {
  return a.r === b.r && a.g === b.g && a.b === b.b && a.a === b.a
}

function floodFill(imageData, newColor, x, y) {
  const {width, height, data} = imageData
  const stack = []
  const baseColor = getColorAtPixel(imageData, x, y)
  let operator = {x, y}

  // Check if base color and new color are the same
  if (colorMatch(baseColor, newColor)) {
    return
  }

  // Add the clicked location to stack
  stack.push({x: operator.x, y: operator.y})

  while (stack.length) {
    operator = stack.pop()
    let contiguousDown = true // Vertical is assumed to be true
    let contiguousUp = true // Vertical is assumed to be true
    let contiguousLeft = false
    let contiguousRight = false

    // Move to top most contiguousDown pixel
    while (contiguousUp && operator.y >= 0) {
      operator.y--
      contiguousUp = colorMatch(getColorAtPixel(imageData, operator.x, operator.y), baseColor)
    }

    // Move downward
    while (contiguousDown && operator.y < height) {
      setColorAtPixel(imageData, newColor, operator.x, operator.y)

      // Check left
      if (operator.x - 1 >= 0 && colorMatch(getColorAtPixel(imageData, operator.x - 1, operator.y), baseColor)) {
        if (!contiguousLeft) {
          contiguousLeft = true
          stack.push({x: operator.x - 1, y: operator.y})
        }
      } else {
        contiguousLeft = false
      }

      // Check right
      if (operator.x + 1 < width && colorMatch(getColorAtPixel(imageData, operator.x + 1, operator.y), baseColor)) {
        if (!contiguousRight) {
          stack.push({x: operator.x + 1, y: operator.y})
          contiguousRight = true
        }
      } else {
        contiguousRight = false
      }

      operator.y++
      contiguousDown = colorMatch(getColorAtPixel(imageData, operator.x, operator.y), baseColor)
    }
  }
}

const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height)

const col = {r: 0xff, g: 0xff, b: 0x0, a: 0xff}

floodFill(imageData, col, 50, 50)
ctx.putImageData(imageData, 0, 0)'''

def fill(x,y):
    global turtle
    display(Javascript(JavaScriptFloodFillCode.replace("drawCanvas","drawCanvas" + str(turtle.canvasNumber))))
    
def startPath():
    javaScriptCode = '\n'.join((
        'var cnv = document.getElementById("drawCanvas' + str(turtle.canvasNumber) + '");',
        'var ctx = cnv.getContext("2d");',
        'ctx.beginPath();'
    ))
    display(Javascript(javaScriptCode))
    
def fillPath():
    javaScriptCode = '\n'.join((
        'var cnv = document.getElementById("drawCanvas' + str(turtle.canvasNumber) + '");',
        'var ctx = cnv.getContext("2d");',
        'ctx.fill();'
    ))
    display(Javascript(javaScriptCode))