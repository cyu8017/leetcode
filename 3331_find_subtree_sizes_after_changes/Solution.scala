// LeetCode 3331 - Find Subtree Sizes After Changes
// https://leetcode.com/problems/find-subtree-sizes-after-changes/

object Solution {
  def findSubtreeSizes(parent: Array[Int], s: String): Array[Int] = {
    val n = parent.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    var i = 1
    while (i < n) {
      g(parent(i)) += i
      i += 1
    }
    val newParent = parent.clone()
    val last = Array.fill(26)(-1)
    def dfs1(u: Int): Unit = {
      val c = s.charAt(u) - 'a'
      val prev = last(c)
      if (prev != -1) newParent(u) = prev
      last(c) = u
      for (v <- g(u)) dfs1(v)
      last(c) = prev
    }
    dfs1(0)
    val ng = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    i = 1
    while (i < n) {
      ng(newParent(i)) += i
      i += 1
    }
    val ans = new Array[Int](n)
    def dfs2(u: Int): Int = {
      var sz = 1
      for (v <- ng(u)) sz += dfs2(v)
      ans(u) = sz
      sz
    }
    dfs2(0)
    ans
  }
}
