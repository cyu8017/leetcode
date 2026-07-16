// LeetCode 0305 - Number of Islands II
// https://leetcode.com/problems/number-of-islands-ii/

import scala.collection.mutable

object Solution {
  private val parent = mutable.Map.empty[Int, Int]
  private val rank = mutable.Map.empty[Int, Int]

  def numIslands2(m: Int, n: Int, positions: Array[Array[Int]]): List[Int] = {
    val result = mutable.ListBuffer.empty[Int]
    var islands = 0
    val directions = Array(Array(1, 0), Array(-1, 0), Array(0, 1), Array(0, -1))

    positions.foreach { position =>
      val row = position(0)
      val col = position(1)
      val index = row * n + col
      if (parent.contains(index)) {
        result += islands
      } else {
        parent(index) = index
        rank(index) = 0
        islands += 1

        directions.foreach { direction =>
          val nextRow = row + direction(0)
          val nextCol = col + direction(1)
          if (nextRow >= 0 && nextRow < m && nextCol >= 0 && nextCol < n) {
            val neighbor = nextRow * n + nextCol
            if (parent.contains(neighbor) && union(index, neighbor)) {
              islands -= 1
            }
          }
        }
        result += islands
      }
    }
    result.toList
  }

  private def find(index: Int): Int = {
    var root = parent(index)
    if (root != index) {
      root = find(root)
      parent(index) = root
    }
    root
  }

  private def union(left: Int, right: Int): Boolean = {
    val rootLeft = find(left)
    val rootRight = find(right)
    if (rootLeft == rootRight) {
      return false
    }
    val leftRank = rank(rootLeft)
    val rightRank = rank(rootRight)
    if (leftRank < rightRank) {
      parent(rootLeft) = rootRight
    } else if (leftRank > rightRank) {
      parent(rootRight) = rootLeft
    } else {
      parent(rootRight) = rootLeft
      rank(rootLeft) = leftRank + 1
    }
    true
  }
}
