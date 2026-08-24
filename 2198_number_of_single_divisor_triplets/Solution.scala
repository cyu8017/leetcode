// LeetCode 2198 - Number of Single Divisor Triplets
// https://leetcode.com/problems/number-of-single-divisor-triplets/

object Solution {
  def singleDivisorTriplet(nums: Array[Int]): Long = {
    val freq = Array.fill(101)(0L)
    for (x <- nums) freq(x) += 1
    var ans = 0L
    var a = 1
    while (a <= 100) {
      if (freq(a) != 0) {
        var b = a
        while (b <= 100) {
          if (freq(b) != 0) {
            var c = b
            while (c <= 100) {
              if (freq(c) != 0) {
                val s = a + b + c
                var cnt = 0
                if (s % a == 0) cnt += 1
                if (s % b == 0) cnt += 1
                if (s % c == 0) cnt += 1
                if (cnt == 1) {
                  if (a == b && b == c) ans += freq(a) * (freq(a) - 1) * (freq(a) - 2)
                  else if (a == b) ans += freq(a) * (freq(a) - 1) * freq(c) * 3
                  else if (b == c) ans += freq(b) * (freq(b) - 1) * freq(a) * 3
                  else if (a == c) ans += freq(a) * (freq(a) - 1) * freq(b) * 3
                  else ans += freq(a) * freq(b) * freq(c) * 6
                }
              }
              c += 1
            }
          }
          b += 1
        }
      }
      a += 1
    }
    ans
  }
}
