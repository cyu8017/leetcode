// LeetCode 3391 - Design a 3D Binary Matrix with Efficient Layer Tracking
// https://leetcode.com/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/

class Matrix3D(_n: Int) {
  private val n = _n
  private val m = Array.fill(n, n, n)(0)
  private val ones = new Array[Int](n)

  def setCell(x: Int, y: Int, z: Int): Unit = {
    if (m(x)(y)(z) == 0) {
      m(x)(y)(z) = 1
      ones(x) += 1
    }
  }

  def unsetCell(x: Int, y: Int, z: Int): Unit = {
    if (m(x)(y)(z) == 1) {
      m(x)(y)(z) = 0
      ones(x) -= 1
    }
  }

  def largestMatrix(): Int = {
    var best = -1
    var idx = 0
    var i = 0
    while (i < n) {
      if (ones(i) >= best) {
        best = ones(i)
        idx = i
      }
      i += 1
    }
    idx
  }
}
