// LeetCode 3011 - Find if Array Can Be Sorted
// https://leetcode.com/problems/find-if-array-can-be-sorted/

object Solution {
  private def popcount(x0: Int): Int = {
    var x = x0
    var c = 0
    while (x != 0) { c += x & 1; x >>= 1 }
    c
  }

  def canSortArray(nums: Array[Int]): Boolean = {
    var preMx = 0
    var i = 0
    val n = nums.length
    while (i < n) {
      val cnt = popcount(nums(i))
      var j = i + 1
      var mi = nums(i)
      var mx = nums(i)
      while (j < n && popcount(nums(j)) == cnt) {
        mi = math.min(mi, nums(j))
        mx = math.max(mx, nums(j))
        j += 1
      }
      if (preMx > mi) return false
      preMx = mx
      i = j
    }
    true
  }
}
