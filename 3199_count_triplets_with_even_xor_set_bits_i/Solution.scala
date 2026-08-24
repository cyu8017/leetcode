// LeetCode 3199 - Count Triplets with Even XOR Set Bits I
// https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-i/

object Solution {
  def tripletCount(a: Array[Int], b: Array[Int], c: Array[Int]): Int = {
    val cnt1 = new Array[Int](2)
    val cnt2 = new Array[Int](2)
    val cnt3 = new Array[Int](2)
    for (x <- a) cnt1(Integer.bitCount(x) % 2) += 1
    for (x <- b) cnt2(Integer.bitCount(x) % 2) += 1
    for (x <- c) cnt3(Integer.bitCount(x) % 2) += 1
    var ans = 0
    var i = 0
    while (i < 2) {
      var j = 0
      while (j < 2) {
        var k = 0
        while (k < 2) {
          if ((i + j + k) % 2 == 0) ans += cnt1(i) * cnt2(j) * cnt3(k)
          k += 1
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
