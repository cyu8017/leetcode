// LeetCode 0457 - Circular Array Loop
// https://leetcode.com/problems/circular-array-loop/

object Solution {
  def circularArrayLoop(nums: Array[Int]): Boolean = {
    val values = nums.clone
    val length = values.length

    def nextIndex(index: Int): Int = {
      val next = index + values(index)
      ((next % length) + length) % length
    }

    for (start <- 0 until length if values(start) != 0) {
      val forward = values(start) > 0
      var slow = start
      var fast = start
      var stop = false

      while (!stop) {
        slow = nextIndex(slow)
        fast = nextIndex(nextIndex(fast))
        if (
          values(slow) * (if (forward) 1 else -1) <= 0 ||
          values(fast) * (if (forward) 1 else -1) <= 0 ||
          values(nextIndex(fast)) * (if (forward) 1 else -1) <= 0
        ) {
          stop = true
        } else if (slow == fast) {
          if (slow == nextIndex(slow)) {
            stop = true
          } else {
            return true
          }
        }
      }

      var index = start
      val direction = values(start)
      while (values(index) * direction > 0) {
        values(index) = 0
        index = nextIndex(index)
      }
    }

    false
  }
}
