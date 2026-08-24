// LeetCode 3556 - Sum of Largest Prime Substrings
// https://leetcode.com/problems/sum-of-largest-prime-substrings/

object Solution {
  def isPrime(x: Long): Boolean = {
    if (x < 2) return false
    val sqrtX = math.sqrt(x.toDouble).toLong
    var i = 2L
    while (i <= sqrtX) {
      if (x % i == 0) return false
      i += 1
    }
    true
  }

  def sumOfLargestPrimes(s: String): Long = {
    val st = new java.util.HashSet[java.lang.Long]()
    val n = s.length
    var i = 0
    while (i < n) {
      var x = 0L
      var j = i
      while (j < n) {
        x = x * 10 + (s.charAt(j) - '0')
        if (isPrime(x)) st.add(x)
        j += 1
      }
      i += 1
    }
    val nums = new java.util.ArrayList[java.lang.Long](st)
    nums.sort(null)
    var ans = 0L
    i = nums.size() - 1
    while (i >= 0 && nums.size() - i <= 3) {
      ans += nums.get(i)
      i -= 1
    }
    ans
  }
}
