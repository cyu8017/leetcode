// LeetCode 1649 - Create Sorted Array through Instructions
// https://leetcode.com/problems/create-sorted-array-through-instructions/

object Solution {
  def createSortedArray(instructions: Array[Int]): Int = {
    val MOD = 1000000007
    val size = (if (instructions.isEmpty) 0 else instructions.max) + 2
    val bit = Array.fill(size + 1)(0)
    def query(i: Int): Int = {
      var s = 0
      var idx = i
      while (idx > 0) {
        s += bit(idx)
        idx -= idx & -idx
      }
      s
    }
    def add(i: Int): Unit = {
      var j = i
      while (j <= size) {
        bit(j) += 1
        j += j & -j
      }
    }
    var ans = 0
    instructions.zipWithIndex.foreach { case (x, i) =>
      ans = (ans + math.min(query(x - 1), i - query(x))) % MOD
      add(x)
    }
    ans
  }
}
