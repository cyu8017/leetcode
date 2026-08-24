// LeetCode 3845 - Maximum Subarray XOR with Bounded Range
// https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/

object Solution {
  private class Node {
    val next = new Array[Int](2)
    var count = 0
  }

  private var nodes: scala.collection.mutable.ArrayBuffer[Node] = _

  private def add(x: Int, delta: Int): Unit = {
    var u = 0
    nodes(u).count += delta
    var b = 15
    while (b >= 0) {
      val bit = (x >> b) & 1
      if (nodes(u).next(bit) == 0) {
        nodes(u).next(bit) = nodes.length
        nodes += new Node
      }
      u = nodes(u).next(bit)
      nodes(u).count += delta
      b -= 1
    }
  }

  private def query(x: Int): Int = {
    var u = 0
    var res = 0
    var b = 15
    while (b >= 0) {
      val bit = (x >> b) & 1
      val want = bit ^ 1
      val v = nodes(u).next(want)
      if (v != 0 && nodes(v).count > 0) {
        res |= 1 << b
        u = v
      } else {
        u = nodes(u).next(bit)
      }
      b -= 1
    }
    res
  }

  def maxSubarrayXor(nums: Array[Int], k: Int): Int = {
    nodes = scala.collection.mutable.ArrayBuffer[Node](new Node)
    val n = nums.length
    val pref = new Array[Int](n + 1)
    var i = 0
    while (i < n) {
      pref(i + 1) = pref(i) ^ nums(i)
      i += 1
    }
    val maxQ = scala.collection.mutable.ArrayBuffer.empty[Int]
    val minQ = scala.collection.mutable.ArrayBuffer.empty[Int]
    var left = 0
    var trieLeft = 0
    var ans = 0
    var r = 0
    while (r < n) {
      val x = nums(r)
      while (maxQ.nonEmpty && nums(maxQ.last) <= x) maxQ.remove(maxQ.length - 1)
      maxQ += r
      while (minQ.nonEmpty && nums(minQ.last) >= x) minQ.remove(minQ.length - 1)
      minQ += r
      while (nums(maxQ(0)) - nums(minQ(0)) > k) {
        if (maxQ(0) == left) maxQ.remove(0)
        if (minQ(0) == left) minQ.remove(0)
        left += 1
      }
      add(pref(r), 1)
      while (trieLeft < left) {
        add(pref(trieLeft), -1)
        trieLeft += 1
      }
      val cur = query(pref(r + 1))
      if (cur > ans) ans = cur
      r += 1
    }
    ans
  }
}
