// LeetCode 3577 - Count the Number of Computer Unlocking Permutations
// https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

object Solution {
  def countPermutations(complexity: Array[Int]): Int = {
    val mod = 1000000007L
    var ans = 1L
    var i = 1
    while (i < complexity.length) {
      if (complexity(i) <= complexity(0)) return 0
      ans = ans * i % mod
      i += 1
    }
    ans.toInt
  }
}
