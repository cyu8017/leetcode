// LeetCode 3079 - Find the Sum of Encrypted Integers
// https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

object Solution {
  def sumOfEncryptedInt(nums: Array[Int]): Int = {
    var ans = 0
    nums.foreach(x => ans += encrypt(x))
    ans
  }

  private def encrypt(x0: Int): Int = {
    var x = x0
    var mx = 0
    var p = 0
    while (x > 0) {
      mx = math.max(mx, x % 10)
      p = p * 10 + 1
      x /= 10
    }
    mx * p
  }
}
