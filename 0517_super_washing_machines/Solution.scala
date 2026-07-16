// LeetCode 0517 - Super Washing Machines
// https://leetcode.com/problems/super-washing-machines/

object Solution {
  def findMinMoves(machines: Array[Int]): Int = {
    val total = machines.sum
    val count = machines.length
    if (total % count != 0) {
      return -1
    }
    val target = total / count
    var prefix = 0
    var result = 0
    for (clothes <- machines) {
      val diff = clothes - target
      prefix += diff
      result = math.max(result, math.max(math.abs(prefix), diff))
    }
    result
  }
}
