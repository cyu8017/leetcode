// LeetCode 0765 - Couples Holding Hands
// https://leetcode.com/problems/couples-holding-hands/

object Solution {
  def minSwapsCouples(row: Array[Int]): Int = {
    val pos = scala.collection.mutable.HashMap.empty[Int, Int]
    var i = 0
    while (i < row.length) {
      pos(row(i)) = i
      i += 1
    }
    var swaps = 0
    i = 0
    while (i < row.length) {
      val partner = row(i) ^ 1
      if (row(i + 1) != partner) {
        val j = pos(partner)
        pos(row(i + 1)) = j
        row(j) = row(i + 1)
        row(i + 1) = partner
        pos(partner) = i + 1
        swaps += 1
      }
      i += 2
    }
    swaps
  }
}
