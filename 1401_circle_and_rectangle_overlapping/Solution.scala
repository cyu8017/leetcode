object Solution {
  def checkOverlap(radius: Int, xCenter: Int, yCenter: Int, x1: Int, y1: Int, x2: Int, y2: Int): Boolean = { val x = math.max(x1, math.min(xCenter, x2)); val y = math.max(y1, math.min(yCenter, y2)); val dx=x-xCenter; val dy=y-yCenter; dx*dx+dy*dy <= radius*radius }
}
