// LeetCode 3337 - Total Characters in String After Transformations II
// https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

object Solution {
  private def matMul(a: Array[Array[Int]], b: Array[Array[Int]], mod: Int): Array[Array[Int]] = {
    val n = a.length
    val c = Array.ofDim[Int](n, n)
    var i = 0
    while (i < n) {
      var k = 0
      while (k < n) {
        if (a(i)(k) != 0) {
          var j = 0
          while (j < n) {
            c(i)(j) = (c(i)(j) + (a(i)(k).toLong * b(k)(j) % mod).toInt) % mod
            j += 1
          }
        }
        k += 1
      }
      i += 1
    }
    c
  }

  private def matPow(a0: Array[Array[Int]], e0: Int, mod: Int): Array[Array[Int]] = {
    val n = a0.length
    var a = a0
    val r = Array.ofDim[Int](n, n)
    var i = 0
    while (i < n) { r(i)(i) = 1; i += 1 }
    var e = e0
    while (e > 0) {
      if ((e & 1) != 0) {
        val nr = matMul(r, a, mod)
        i = 0
        while (i < n) { Array.copy(nr(i), 0, r(i), 0, n); i += 1 }
      }
      a = matMul(a, a, mod)
      e >>= 1
    }
    r
  }

  def lengthAfterTransformations(s: String, t: Int, nums: Array[Int]): Int = {
    val mod = 1000000007
    var mat = Array.ofDim[Int](26, 26)
    var i = 0
    while (i < 26) {
      var j = 1
      while (j <= nums(i)) {
        mat(i)((i + j) % 26) = 1
        j += 1
      }
      i += 1
    }
    mat = matPow(mat, t, mod)
    val cnt = new Array[Int](26)
    for (c <- s) cnt(c - 'a') += 1
    var ans = 0
    i = 0
    while (i < 26) {
      var j = 0
      while (j < 26) {
        ans = (ans + (cnt(i).toLong * mat(i)(j) % mod).toInt) % mod
        j += 1
      }
      i += 1
    }
    ans
  }
}
