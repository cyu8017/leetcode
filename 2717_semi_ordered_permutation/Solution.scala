// LeetCode 2717 - Semi-Ordered Permutation
// https://leetcode.com/problems/semi-ordered-permutation/

object Solution {
  def semiOrderedPermutation(nums: Array[Int]): Int = {
    val n = nums.length
    var p1 = 0
    var pn = 0
    var i = 0
    while (i < n) {
      if (nums(i) == 1) p1 = i
      if (nums(i) == n) pn = i
      i += 1
    }
    var ans = p1 + (n - 1 - pn)
    if (p1 > pn) ans -= 1
    ans
  }
}
