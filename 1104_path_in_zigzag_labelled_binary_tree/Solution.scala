// LeetCode 1104 - Path In Zigzag Labelled Binary Tree
// https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

object Solution {
  def pathInZigZagTree(label: Int): List[Int] = {
    val path = scala.collection.mutable.ListBuffer(label)
    var cur = label
    while (cur > 1) {
      val level = Integer.numberOfTrailingZeros(Integer.highestOneBit(cur))
      cur >>= 1
      cur = (1 << level) - 1 - cur + (1 << (level - 1))
      path += cur
    }
    path.reverse.toList
  }
}
