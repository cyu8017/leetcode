// LeetCode 2791 - Count Paths That Can Form a Palindrome in a Tree
// https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/

object Solution {
  def countPalindromePaths(parent: List[Int], s: String): Long = {
    val n = parent.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    var i = 1
    while (i < n) {
      g(parent(i)) += i
      i += 1
    }
    val freq = scala.collection.mutable.Map(0 -> 1)
    var ans = 0L
    def dfs(u: Int, mask: Int): Unit = {
      g(u).foreach { v =>
        val nm = mask ^ (1 << (s.charAt(v) - 'a'))
        ans += freq.getOrElse(nm, 0)
        var b = 0
        while (b < 26) {
          ans += freq.getOrElse(nm ^ (1 << b), 0)
          b += 1
        }
        freq(nm) = freq.getOrElse(nm, 0) + 1
        dfs(v, nm)
      }
    }
    dfs(0, 0)
    ans
  }
}
