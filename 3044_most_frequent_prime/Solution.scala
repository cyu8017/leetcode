// LeetCode 3044 - Most Frequent Prime
// https://leetcode.com/problems/most-frequent-prime/

object Solution {
  private def isPrime(n: Int): Boolean = {
    if (n < 2) return false
    var i = 2
    while (i <= n / i) {
      if (n % i == 0) return false
      i += 1
    }
    true
  }

  def mostFrequentPrime(mat: Array[Array[Int]]): Int = {
    val m = mat.length
    val n = mat(0).length
    val cnt = scala.collection.mutable.HashMap[Int, Int]()
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        var a = -1
        while (a <= 1) {
          var b = -1
          while (b <= 1) {
            if (!(a == 0 && b == 0)) {
              var x = i + a
              var y = j + b
              var v = mat(i)(j)
              while (x >= 0 && x < m && y >= 0 && y < n) {
                v = v * 10 + mat(x)(y)
                if (isPrime(v)) cnt(v) = cnt.getOrElse(v, 0) + 1
                x += a
                y += b
              }
            }
            b += 1
          }
          a += 1
        }
        j += 1
      }
      i += 1
    }
    var ans = -1
    var mx = 0
    for ((key, value) <- cnt) {
      if (mx < value || (mx == value && ans < key)) {
        mx = value
        ans = key
      }
    }
    ans
  }
}
