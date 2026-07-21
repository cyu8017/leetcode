// LeetCode 1842 - Next Palindrome Using Same Digits
// https://leetcode.com/problems/next-palindrome-using-same-digits/

object Solution {
  def nextPalindrome(num: String): String = {
    val nums = num.toArray
    if (!nextPermutation(nums)) return ""
    val n = nums.length
    for (i <- 0 until n / 2) nums(n - i - 1) = nums(i)
    new String(nums)
  }

  private def nextPermutation(nums: Array[Char]): Boolean = {
    val n = nums.length / 2
    var i = n - 2
    while (i >= 0 && nums(i) >= nums(i + 1)) i -= 1
    if (i < 0) return false
    var j = n - 1
    while (nums(j) <= nums(i)) j -= 1
    val tmp = nums(i); nums(i) = nums(j); nums(j) = tmp
    var l = i + 1
    var r = n - 1
    while (l < r) {
      val t = nums(l); nums(l) = nums(r); nums(r) = t
      l += 1; r -= 1
    }
    true
  }
}
