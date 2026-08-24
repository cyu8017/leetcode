// LeetCode 2959 - Number of Possible Sets of Closing Branches
// https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/

object Solution {
  def numberOfSets(n: Int, maxDistance: Int, roads: Array[Array[Int]]): Int = {
    var ans = 0
    var mask = 0
    while (mask < (1 << n)) {
      val dist = Array.fill(n, n)(1 << 29)
      var i = 0
      while (i < n) { dist(i)(i) = 0; i += 1 }
      for (r <- roads) {
        val u = r(0)
        val v = r(1)
        val w = r(2)
        if ((mask & (1 << u)) != 0 && (mask & (1 << v)) != 0) {
          if (w < dist(u)(v)) {
            dist(u)(v) = w
            dist(v)(u) = w
          }
        }
      }
      var k = 0
      while (k < n) {
        if ((mask & (1 << k)) != 0) {
          i = 0
          while (i < n) {
            if ((mask & (1 << i)) != 0) {
              var j = 0
              while (j < n) {
                if ((mask & (1 << j)) != 0 && dist(i)(k) + dist(k)(j) < dist(i)(j))
                  dist(i)(j) = dist(i)(k) + dist(k)(j)
                j += 1
              }
            }
            i += 1
          }
        }
        k += 1
      }
      var ok = true
      i = 0
      while (i < n && ok) {
        if ((mask & (1 << i)) != 0) {
          var j = 0
          while (j < n) {
            if ((mask & (1 << j)) != 0 && dist(i)(j) > maxDistance) { ok = false }
            j += 1
          }
        }
        i += 1
      }
      if (ok) ans += 1
      mask += 1
    }
    ans
  }
}
