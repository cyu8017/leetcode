// LeetCode 2098 - Subsequence of Size K With the Largest Even Sum
// https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/

object Solution {
  def largestEvenSum(nums: Array[Int], k: Int): Long = {
    val arr = nums.sorted(Ordering[Int].reverse)
    var sum = 0L
    var i = 0
    while (i < k) {
      sum += arr(i)
      i += 1
    }
    if (sum % 2 == 0) return sum
    var ans = -1L
    var oddIn = -1
    var evenIn = -1
    var oddOut = -1
    var evenOut = -1
    i = k - 1
    while (i >= 0) {
      if (arr(i) % 2 != 0 && oddIn == -1) oddIn = i
      if (arr(i) % 2 == 0 && evenIn == -1) evenIn = i
      i -= 1
    }
    i = k
    while (i < arr.length) {
      if (arr(i) % 2 != 0 && oddOut == -1) oddOut = i
      if (arr(i) % 2 == 0 && evenOut == -1) evenOut = i
      i += 1
    }
    if (oddIn != -1 && evenOut != -1) ans = math.max(ans, sum - arr(oddIn) + arr(evenOut))
    if (evenIn != -1 && oddOut != -1) ans = math.max(ans, sum - arr(evenIn) + arr(oddOut))
    ans
  }
}
