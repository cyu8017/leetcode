// LeetCode 3162 - Find the Number of Good Pairs I
// https://leetcode.com/problems/find-the-number-of-good-pairs-i/

object Solution {
  def numberOfPairs(nums1: Array[Int], nums2: Array[Int], k: Int): Int = {
    var ans = 0
    nums1.foreach { x =>
      nums2.foreach { y =>
        if (x % (y * k) == 0) ans += 1
      }
    }
    ans
  }
}
