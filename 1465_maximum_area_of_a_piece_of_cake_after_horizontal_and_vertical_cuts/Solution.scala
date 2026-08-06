object Solution {
  def maxArea(h: Int, w: Int, horizontalCuts: Array[Int], verticalCuts: Array[Int]): Int = {
    val hs = (Array(0, h) ++ horizontalCuts).sorted
    val vs = (Array(0, w) ++ verticalCuts).sorted
    val maxH = hs.sliding(2).map(pair => pair(1) - pair(0)).max
    val maxV = vs.sliding(2).map(pair => pair(1) - pair(0)).max
    ((maxH.toLong * maxV) % 1000000007L).toInt
  }
}
