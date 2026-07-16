// LeetCode 0356 - Line Reflection

// https://leetcode.com/problems/line-reflection/



object Solution {

  def isReflected(points: Array[Array[Int]]): Boolean = {

    val pointSet = points.map(point => s"${point(0)},${point(1)}").toSet

    val xs = points.map(_(0))

    val minX = xs.min

    val maxX = xs.max

    val target = minX + maxX



    points.forall { point =>

      pointSet.contains(s"${target - point(0)},${point(1)}")

    }

  }

}
