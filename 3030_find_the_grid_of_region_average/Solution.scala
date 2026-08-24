// LeetCode 3030 - Find the Grid of Region Average
// https://leetcode.com/problems/find-the-grid-of-region-average/

object Solution {
  def resultGrid(image: Array[Array[Int]], threshold: Int): Array[Array[Int]] = {
    val n = image.length
    val m = image(0).length
    val ans = Array.ofDim[Int](n, m)
    val ct = Array.ofDim[Int](n, m)
    var i = 0
    while (i + 2 < n) {
      var j = 0
      while (j + 2 < m) {
        var region = true
        var k = 0
        while (k < 3) {
          var l = 0
          while (l < 2) {
            region = region && math.abs(image(i + k)(j + l) - image(i + k)(j + l + 1)) <= threshold
            l += 1
          }
          k += 1
        }
        k = 0
        while (k < 2) {
          var l = 0
          while (l < 3) {
            region = region && math.abs(image(i + k)(j + l) - image(i + k + 1)(j + l)) <= threshold
            l += 1
          }
          k += 1
        }
        if (region) {
          var tot = 0
          k = 0
          while (k < 3) {
            var l = 0
            while (l < 3) { tot += image(i + k)(j + l); l += 1 }
            k += 1
          }
          k = 0
          while (k < 3) {
            var l = 0
            while (l < 3) {
              ct(i + k)(j + l) += 1
              ans(i + k)(j + l) += tot / 9
              l += 1
            }
            k += 1
          }
        }
        j += 1
      }
      i += 1
    }
    i = 0
    while (i < n) {
      var j = 0
      while (j < m) {
        if (ct(i)(j) == 0) ans(i)(j) = image(i)(j)
        else ans(i)(j) /= ct(i)(j)
        j += 1
      }
      i += 1
    }
    ans
  }
}
