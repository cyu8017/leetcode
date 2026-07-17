// LeetCode 1720 - Decode XORed Array
// https://leetcode.com/problems/decode-xored-array/

object Solution {
  def decode(encoded: Array[Int], first: Int): Array[Int] = {
    val ans = new Array[Int](encoded.length + 1)
    ans(0) = first
    for (i <- encoded.indices) {
      ans(i + 1) = ans(i) ^ encoded(i)
    }
    ans
  }
}
