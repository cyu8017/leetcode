// LeetCode 0666 - Path Sum IV
// https://leetcode.com/problems/path-sum-iv/

import scala.collection.mutable

object Solution {
  def pathSum(nums: Array[Int]): Int = {
    val tree = mutable.Map.empty[Long, Int]
    var total = 0
    nums.foreach(num => tree(key(num / 100, (num / 10) % 10)) = num % 10)
    def dfs(depth: Int, pos: Int, path0: Int): Unit = {
      val k = key(depth, pos)
      if (!tree.contains(k)) return
      val path = path0 + tree(k)
      val left = key(depth + 1, pos * 2 - 1)
      val right = key(depth + 1, pos * 2)
      if (!tree.contains(left) && !tree.contains(right)) {
        total += path
        return
      }
      dfs(depth + 1, pos * 2 - 1, path)
      dfs(depth + 1, pos * 2, path)
    }
    dfs(1, 1, 0)
    total
  }

  private def key(depth: Int, pos: Int): Long =
    (depth.toLong << 32) | (pos.toLong & 0xffffffffL)
}
