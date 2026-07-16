// LeetCode 0391 - Perfect Rectangle

// https://leetcode.com/problems/perfect-rectangle/



import scala.collection.mutable



object Solution {

  def isRectangleCover(rectangles: Array[Array[Int]]): Boolean = {

    val points = mutable.Set.empty[Long]

    var area = 0L

    var minX = Int.MaxValue

    var minY = Int.MaxValue

    var maxX = Int.MinValue

    var maxY = Int.MinValue



    for (rectangle <- rectangles) {

      val x1 = rectangle(0)

      val y1 = rectangle(1)

      val x2 = rectangle(2)

      val y2 = rectangle(3)

      area += (x2 - x1).toLong * (y2 - y1)

      minX = math.min(minX, x1)

      minY = math.min(minY, y1)

      maxX = math.max(maxX, x2)

      maxY = math.max(maxY, y2)



      for ((x, y) <- Seq((x1, y1), (x1, y2), (x2, y1), (x2, y2))) {

        val point = encode(x, y)

        if (points.contains(point)) {

          points.remove(point)

        } else {

          points.add(point)

        }

      }

    }



    val expectedCorners = Set(

      encode(minX, minY),

      encode(minX, maxY),

      encode(maxX, minY),

      encode(maxX, maxY),

    )

    if (points.toSet != expectedCorners) {

      return false

    }



    area == (maxX - minX).toLong * (maxY - minY)

  }



  private def encode(x: Int, y: Int): Long =

    (x.toLong << 32) | (y.toLong & 0xffffffffL)

}
