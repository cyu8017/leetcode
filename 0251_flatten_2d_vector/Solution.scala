// LeetCode 0251 - Flatten 2D Vector
// https://leetcode.com/problems/flatten-2d-vector/

class Vector2D(vec: Array[Array[Int]]) {
  private val vec = vec
  private var row = 0
  private var col = 0
  advance()

  def next(): Int = {
    val value = vec(row)(col)
    col += 1
    advance()
    value
  }

  def hasNext(): Boolean = {
    advance()
    row < vec.length
  }

  private def advance(): Unit = {
    while (row < vec.length && col >= vec(row).length) {
      row += 1
      col = 0
    }
  }
}
