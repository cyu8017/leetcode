// LeetCode 3242 - Design Neighbor Sum Service
// https://leetcode.com/problems/design-neighbor-sum-service/

class NeighborSum(_grid: Array[Array[Int]]) {
  private val grid = _grid
  private val d = scala.collection.mutable.HashMap.empty[Int, Array[Int]]
  private val dirs = Array(
    Array(-1, 0, 1, 0, -1),
    Array(-1, 1, 1, -1, -1)
  )
  var i = 0
  while (i < grid.length) {
    var j = 0
    while (j < grid(i).length) {
      d(grid(i)(j)) = Array(i, j)
      j += 1
    }
    i += 1
  }

  private def cal(value: Int, k: Int): Int = {
    val p = d(value)
    var s = 0
    var q = 0
    while (q < 4) {
      val x = p(0) + dirs(k)(q)
      val y = p(1) + dirs(k)(q + 1)
      if (x >= 0 && x < grid.length && y >= 0 && y < grid(0).length) s += grid(x)(y)
      q += 1
    }
    s
  }

  def adjacentSum(value: Int): Int = cal(value, 0)
  def diagonalSum(value: Int): Int = cal(value, 1)
}
