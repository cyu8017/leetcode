// LeetCode 2420 - Find All Good Indices
// https://leetcode.com/problems/find-all-good-indices/

object Solution {
  def goodIndices(nums: Array[Int], k: Int): List[Int] = {
    val n = nums.length
    val dec = new Array[Int](n)
    val inc = new Array[Int](n)
    dec(0) = 1
    var i = 1
    while (i < n) {
      dec(i) = if (nums(i) <= nums(i - 1)) dec(i - 1) + 1 else 1
      i += 1
    }
    inc(n - 1) = 1
    i = n - 2
    while (i >= 0) {
      inc(i) = if (nums(i) <= nums(i + 1)) inc(i + 1) + 1 else 1
      i -= 1
    }
    val ans = scala.collection.mutable.ListBuffer.empty[Int]
    i = k
    while (i < n - k) {
      if (dec(i - 1) >= k && inc(i + 1) >= k) ans += i
      i += 1
    }
    ans.toList
  }
}
