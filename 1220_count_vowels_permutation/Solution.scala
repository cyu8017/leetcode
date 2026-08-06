// LeetCode 1220 - Count Vowels Permutation
// https://leetcode.com/problems/count-vowels-permutation/

object Solution {
  def countVowelPermutation(n: Int): Int = {
    val mod = 1000000007
    var a, e, i, o, u = 1L
    for (_ <- 1 until n) {
      val na = (e + i + u) % mod
      val ne = (a + i) % mod
      val ni = (e + o) % mod
      val no = i
      val nu = (i + o) % mod
      a = na; e = ne; i = ni; o = no; u = nu
    }
    ((a + e + i + o + u) % mod).toInt
  }
}
