// LeetCode 1860 - Incremental Memory Leak
// https://leetcode.com/problems/incremental-memory-leak/

object Solution {
  def memLeak(memory1: Int, memory2: Int): Array[Int] = {
    var m1 = memory1
    var m2 = memory2
    var second = 1
    while (m1 >= second || m2 >= second) {
      if (m1 >= m2) m1 -= second
      else m2 -= second
      second += 1
    }
    Array(second, m1, m2)
  }
}
