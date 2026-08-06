// LeetCode 1580 - Put Boxes Into the Warehouse II
// https://leetcode.com/problems/put-boxes-into-the-warehouse-ii/

object Solution {
  def maxBoxesInWarehouse(boxes: Array[Int], warehouse: Array[Int]): Int = {
    val n = warehouse.length
    val left = warehouse.clone()
    val right = warehouse.clone()
    for (i <- 1 until n) left(i) = math.min(left(i), left(i - 1))
    for (i <- n - 2 to 0 by -1) right(i) = math.min(right(i), right(i + 1))
    val capacity = (0 until n).map(i => math.max(left(i), right(i))).sorted
    val sortedBoxes = boxes.sorted
    var i = 0
    for (room <- capacity if i < sortedBoxes.length && sortedBoxes(i) <= room) i += 1
    i
  }
}
