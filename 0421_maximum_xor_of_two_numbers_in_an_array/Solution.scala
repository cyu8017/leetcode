// LeetCode 0421 - Maximum XOR of Two Numbers in an Array
// https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

import scala.collection.mutable

object Solution {
  private class TrieNode(children: mutable.Map[Int, TrieNode] = mutable.Map.empty) {
    val childMap: mutable.Map[Int, TrieNode] = children
  }

  def findMaximumXOR(nums: Array[Int]): Int = {
    val maximum = nums.max
    val maxBit = if (maximum == 0) 0 else 32 - Integer.numberOfLeadingZeros(maximum)
    val root = new TrieNode()
    var best = 0

    for (number <- nums) {
      var node = root
      for (bit <- maxBit - 1 to 0 by -1) {
        val current = (number >> bit) & 1
        node = node.childMap.getOrElseUpdate(current, new TrieNode())
      }
    }

    for (number <- nums) {
      var node = root
      var candidate = 0
      for (bit <- maxBit - 1 to 0 by -1) {
        val current = (number >> bit) & 1
        val target = 1 - current
        if (node.childMap.contains(target)) {
          candidate |= 1 << bit
          node = node.childMap(target)
        } else {
          node = node.childMap(current)
        }
      }
      best = math.max(best, candidate)
    }

    best
  }
}
