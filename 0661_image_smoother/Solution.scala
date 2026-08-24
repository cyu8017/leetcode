// LeetCode 0661 - Image Smoother
// https://leetcode.com/problems/image-smoother/

object Solution {
  def imageSmoother(img: Array[Array[Int]]): Array[Array[Int]] = {
    val m = img.length
    val n = img(0).length
    val out = Array.ofDim[Int](m, n)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        var total = 0
        var count = 0
        var di = -1
        while (di <= 1) {
          var dj = -1
          while (dj <= 1) {
            val ni = i + di
            val nj = j + dj
            if (ni >= 0 && ni < m && nj >= 0 && nj < n) {
              total += img(ni)(nj)
              count += 1
            }
            dj += 1
          }
          di += 1
        }
        out(i)(j) = total / count
        j += 1
      }
      i += 1
    }
    out
  }
}
