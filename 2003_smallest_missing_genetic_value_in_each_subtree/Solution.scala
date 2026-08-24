// LeetCode 2003 - Smallest Missing Genetic Value in Each Subtree
// https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/

object Solution {
  def smallestMissingValueSubtree(parents: Array[Int], nums: Array[Int]): Array[Int] = {
    val n = parents.length
    val children = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    var i = 1
    while (i < n) {
      children(parents(i)) += i
      i += 1
    }
    val ans = Array.fill(n)(1)
    var one = -1
    i = 0
    while (i < n) {
      if (nums(i) == 1) { one = i; i = n }
      else i += 1
    }
    if (one < 0) return ans
    val seen = scala.collection.mutable.HashSet.empty[Int]
    def collect(u: Int): Unit = {
      if (seen.contains(nums(u))) return
      seen += nums(u)
      children(u).foreach(collect)
    }
    var miss = 1
    var node = one
    var prev = -1
    while (node != -1) {
      children(node).foreach { v => if (v != prev) collect(v) }
      seen += nums(node)
      while (seen.contains(miss)) miss += 1
      ans(node) = miss
      prev = node
      node = parents(node)
    }
    ans
  }
}
