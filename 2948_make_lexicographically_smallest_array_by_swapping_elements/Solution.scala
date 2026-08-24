// LeetCode 2948 - Make Lexicographically Smallest Array by Swapping Elements
// https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

object Solution {
  def lexicographicallySmallestArray(nums: Array[Int], limit: Int): Array[Int] = {
    val n = nums.length
    val idx = Array.tabulate(n)(identity)
    scala.util.Sorting.stableSort(idx, (a: Int, b: Int) => nums(a) < nums(b) || (nums(a) == nums(b) && a < b))
    val ans = Array.ofDim[Int](n)
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n && nums(idx(j)) - nums(idx(j - 1)) <= limit) j += 1
      val groupIdx = Array.tabulate(j - i)(t => idx(i + t))
      scala.util.Sorting.quickSort(groupIdx)
      var t = 0
      while (t < j - i) {
        ans(groupIdx(t)) = nums(idx(i + t))
        t += 1
      }
      i = j
    }
    ans
  }
}
