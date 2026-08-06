// LeetCode 1564 - Put Boxes Into the Warehouse I
// https://leetcode.com/problems/put-boxes-into-the-warehouse-i/

object Solution {
  def maxBoxesInWarehouse(boxes: Array[Int], warehouse: Array[Int]): Int = {
    val wh = warehouse.clone()
    for (i <- 1 until wh.length) wh(i) = math.min(wh(i), wh(i - 1))
    val sorted = boxes.sorted
    var room = wh.length - 1
    var used = 0
    for (box <- sorted if room >= 0) {
      while (room >= 0 && wh(room) < box) room -= 1
      if (room >= 0) {
        used += 1
        room -= 1
      }
    }
    used
  }
}
