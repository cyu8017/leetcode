// LeetCode 2916 - Subarrays Distinct Element Sum of Squares II
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/

object Solution {
  private val MOD = 1000000007
  private var tree: Array[Node] = _

  private class Node {
    var sum: Int = 0
    var sumSq: Int = 0
    var lazy: Int = 0
  }

  def sumCounts(nums: Array[Int]): Int = {
    val n = nums.length
    val last = scala.collection.mutable.Map.empty[Int, Int]
    tree = Array.fill(4 * (n + 2))(new Node)
    var ans = 0
    for (i <- 1 to n) {
      val v = nums(i - 1)
      val prev = last.getOrElse(v, 0)
      update(1, 1, n, prev + 1, i, 1)
      ans = (ans + tree(1).sumSq) % MOD
      last(v) = i
    }
    ans
  }

  private def apply(idx: Int, l: Int, r: Int, value: Int): Unit = {
    val length = r - l + 1
    tree(idx).sumSq = ((tree(idx).sumSq + 2L * value % MOD * tree(idx).sum % MOD
      + 1L * value % MOD * value % MOD * length % MOD) % MOD).toInt
    tree(idx).sum = ((tree(idx).sum + 1L * value % MOD * length % MOD) % MOD).toInt
    tree(idx).lazy = (tree(idx).lazy + value) % MOD
  }

  private def update(idx: Int, l: Int, r: Int, ql: Int, qr: Int, value: Int): Unit = {
    if (ql > r || qr < l) return
    if (ql <= l && r <= qr) {
      apply(idx, l, r, value)
      return
    }
    if (tree(idx).lazy != 0 && l != r) {
      val mid = (l + r) / 2
      apply(idx * 2, l, mid, tree(idx).lazy)
      apply(idx * 2 + 1, mid + 1, r, tree(idx).lazy)
      tree(idx).lazy = 0
    }
    val mid = (l + r) / 2
    update(idx * 2, l, mid, ql, qr, value)
    update(idx * 2 + 1, mid + 1, r, ql, qr, value)
    tree(idx).sum = (tree(idx * 2).sum + tree(idx * 2 + 1).sum) % MOD
    tree(idx).sumSq = (tree(idx * 2).sumSq + tree(idx * 2 + 1).sumSq) % MOD
  }
}
