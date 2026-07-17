// LeetCode 1764 - Form Array by Concatenating Subarrays of Another Array
// https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/

object Solution {
  def canChoose(groups: Array[Array[Int]], nums: Array[Int]): Boolean = {
    val n = nums.length

    def matches(start: Int, g: Array[Int]): Boolean = {
      var t = 0
      while (t < g.length) {
        if (nums(start + t) != g(t)) return false
        t += 1
      }
      true
    }

    def dfs(i: Int, start: Int): Boolean = {
      if (i == groups.length) {
        return start == n
      }
      val g = groups(i)
      val m = g.length
      var j = start
      while (j <= n - m) {
        if (matches(j, g) && dfs(i + 1, j + m)) return true
        j += 1
      }
      false
    }

    dfs(0, 0)
  }
}
