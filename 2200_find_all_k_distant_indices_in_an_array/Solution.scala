// LeetCode 2200 - Find All K-Distant Indices in an Array
// https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

object Solution {
  def findKDistantIndices(nums: Array[Int], key: Int, k: Int): List[Int] = {
    val n = nums.length
    val mark = Array.fill(n)(false)
    var i = 0
    while (i < n) {
      if (nums(i) == key) {
        val l = math.max(0, i - k)
        val r = math.min(n - 1, i + k)
        var j = l
        while (j <= r) {
          mark(j) = true
          j += 1
        }
      }
      i += 1
    }
    val ans = scala.collection.mutable.ListBuffer.empty[Int]
    i = 0
    while (i < n) {
      if (mark(i)) ans += i
      i += 1
    }
    ans.toList
  }
}
