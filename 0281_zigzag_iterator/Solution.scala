// LeetCode 0281 - Zigzag Iterator
// https://leetcode.com/problems/zigzag-iterator/

class ZigzagIterator(v1: Array[Int], v2: Array[Int]) {
  private val vectors = Array(v1, v2)
  private val indices = Array(0, 0)
  private var turn = 0

  def next(): Int = {
    while (indices(turn) >= vectors(turn).length) {
      turn = 1 - turn
    }
    val value = vectors(turn)(indices(turn))
    indices(turn) += 1
    turn = 1 - turn
    value
  }

  def hasNext(): Boolean =
    indices.zip(vectors).exists { case (index, vector) => index < vector.length }
}
