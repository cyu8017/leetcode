// LeetCode 3469 - Find Minimum Cost to Remove Array Elements
// https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements/

object Solution {
  private val memo = new java.util.HashMap[java.lang.Long, Integer]()
  private var nums: Array[Int] = _
  private var n = 0

  private def max2(a: Int, b: Int): Int = if (a > b) a else b
  private def min3(a: Int, b: Int, c: Int): Int = math.min(a, math.min(b, c))
  private def key(i: Int, prev: Int): Long = (i.toLong << 32) | (prev & 0xffffffffL)

  private def dfs(i: Int, prev: Int): Int = {
    if (i >= n) return if (prev == -1) 0 else nums(prev)
    val k = key(i, prev)
    val cached = memo.get(k)
    if (cached != null) return cached
    val res =
      if (prev == -1) {
        if (i + 1 >= n) nums(i)
        else if (i + 2 >= n) max2(nums(i), nums(i + 1))
        else {
          val a = nums(i)
          val b = nums(i + 1)
          val c = nums(i + 2)
          min3(max2(b, c) + dfs(i + 3, i), max2(a, c) + dfs(i + 3, i + 1), max2(a, b) + dfs(i + 3, i + 2))
        }
      } else {
        if (i + 1 >= n) max2(nums(prev), nums(i))
        else {
          val a = nums(prev)
          val b = nums(i)
          val c = nums(i + 1)
          min3(max2(b, c) + dfs(i + 2, prev), max2(a, c) + dfs(i + 2, i), max2(a, b) + dfs(i + 2, i + 1))
        }
      }
    memo.put(k, res)
    res
  }

  def minCost(nums0: Array[Int]): Int = {
    nums = nums0
    n = nums.length
    memo.clear()
    dfs(0, -1)
  }
}
