// LeetCode 2213 - Longest Substring of One Repeating Character
// https://leetcode.com/problems/longest-substring-of-one-repeating-character/

object Solution {
  private class Seg {
    var lChar: Char = 0
    var rChar: Char = 0
    var lLen: Int = 0
    var rLen: Int = 0
    var best: Int = 0
    var size: Int = 0
  }

  def longestRepeating(s_ : String, queryCharacters: String, queryIndices: Array[Int]): Array[Int] = {
    def merge(a: Seg, b: Seg): Seg = {
      if (a.size == 0) return b
      if (b.size == 0) return a
      val res = new Seg
      res.lChar = a.lChar
      res.rChar = b.rChar
      res.size = a.size + b.size
      res.best = math.max(a.best, b.best)
      res.lLen = a.lLen
      res.rLen = b.rLen
      if (a.rChar == b.lChar) {
        val mid = a.rLen + b.lLen
        res.best = math.max(res.best, mid)
        if (a.lLen == a.size) res.lLen = a.size + b.lLen
        if (b.rLen == b.size) res.rLen = b.size + a.rLen
      }
      res
    }
    val s = s_.toCharArray
    val n = s.length
    val tree = new Array[Seg](4 * n + 5)
    def build(idx: Int, l: Int, r: Int): Unit = {
      if (l == r) {
        tree(idx) = new Seg
        tree(idx).lChar = s(l)
        tree(idx).rChar = s(l)
        tree(idx).lLen = 1
        tree(idx).rLen = 1
        tree(idx).best = 1
        tree(idx).size = 1
        return
      }
      val mid = (l + r) / 2
      build(idx * 2, l, mid)
      build(idx * 2 + 1, mid + 1, r)
      tree(idx) = merge(tree(idx * 2), tree(idx * 2 + 1))
    }
    def update(idx: Int, l: Int, r: Int, pos: Int, ch: Char): Unit = {
      if (l == r) {
        s(pos) = ch
        tree(idx) = new Seg
        tree(idx).lChar = ch
        tree(idx).rChar = ch
        tree(idx).lLen = 1
        tree(idx).rLen = 1
        tree(idx).best = 1
        tree(idx).size = 1
        return
      }
      val mid = (l + r) / 2
      if (pos <= mid) update(idx * 2, l, mid, pos, ch)
      else update(idx * 2 + 1, mid + 1, r, pos, ch)
      tree(idx) = merge(tree(idx * 2), tree(idx * 2 + 1))
    }
    build(1, 0, n - 1)
    val ans = new Array[Int](queryIndices.length)
    var i = 0
    while (i < queryIndices.length) {
      update(1, 0, n - 1, queryIndices(i), queryCharacters.charAt(i))
      ans(i) = tree(1).best
      i += 1
    }
    ans
  }
}
