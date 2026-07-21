// LeetCode 1803 - Count Pairs With XOR in a Range
// https://leetcode.com/problems/count-pairs-with-xor-in-a-range/

object Solution {
  private class TrieNode {
    var count = 0
    val children = Array.fill[TrieNode](2)(null)
  }

  def countPairs(nums: Array[Int], low: Int, high: Int): Int =
    countSmallerThan(nums, high + 1) - countSmallerThan(nums, low)

  private def countSmallerThan(nums: Array[Int], limit: Int): Int = {
    if (limit <= 0) return 0
    val root = new TrieNode
    var total = 0
    val maxBit = 15
    for (num <- nums) {
      total += query(root, num, limit, maxBit)
      insert(root, num, maxBit)
    }
    total
  }

  private def insert(root: TrieNode, num: Int, bit: Int): Unit = {
    var node = root
    var i = bit
    while (i >= 0) {
      val b = (num >> i) & 1
      if (node.children(b) == null) node.children(b) = new TrieNode
      node = node.children(b)
      node.count += 1
      i -= 1
    }
  }

  private def query(root: TrieNode, num: Int, limit: Int, bit: Int): Int = {
    if (root == null || bit < 0) return 0
    val numBit = (num >> bit) & 1
    val limitBit = (limit >> bit) & 1
    val child = root.children(numBit)
    if (limitBit == 1) {
      val same = if (child != null) child.count else 0
      same + query(root.children(1 - numBit), num, limit, bit - 1)
    } else {
      query(child, num, limit, bit - 1)
    }
  }
}
