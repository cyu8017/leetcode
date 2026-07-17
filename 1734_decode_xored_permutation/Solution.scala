// LeetCode 1734 - Decode XORed Permutation
// https://leetcode.com/problems/decode-xored-permutation/

object Solution {
  def decode(encoded: Array[Int]): Array[Int] = {
    val n = encoded.length + 1
    var total = 0
    for (value <- 1 to n) {
      total ^= value
    }
    var odd = 0
    var i = 1
    while (i < encoded.length) {
      odd ^= encoded(i)
      i += 2
    }
    val ans = new Array[Int](n)
    ans(0) = total ^ odd
    for (j <- encoded.indices) {
      ans(j + 1) = ans(j) ^ encoded(j)
    }
    ans
  }
}
