// LeetCode 2018 - Check if Word Can Be Placed In Crossword
// https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/

object Solution {
  def placeWordInCrossword(board: Array[Array[Char]], word: String): Boolean = {
    val m = board.length
    val n = board(0).length
    val L = word.length
    def matchCells(cells: String): Boolean = {
      if (cells.length != L) return false
      var ok1 = true
      var ok2 = true
      var i = 0
      while (i < L) {
        if (cells.charAt(i) != ' ' && cells.charAt(i) != word.charAt(i)) ok1 = false
        if (cells.charAt(i) != ' ' && cells.charAt(i) != word.charAt(L - 1 - i)) ok2 = false
        i += 1
      }
      ok1 || ok2
    }
    var r = 0
    while (r < m) {
      var c = 0
      while (c < n) {
        while (c < n && board(r)(c) == '#') c += 1
        val start = c
        while (c < n && board(r)(c) != '#') c += 1
        if (c - start == L) {
          val sb = new StringBuilder
          var i = start
          while (i < c) { sb.append(board(r)(i)); i += 1 }
          if (matchCells(sb.toString)) return true
        }
      }
      r += 1
    }
    var c = 0
    while (c < n) {
      r = 0
      while (r < m) {
        while (r < m && board(r)(c) == '#') r += 1
        val start = r
        while (r < m && board(r)(c) != '#') r += 1
        if (r - start == L) {
          val sb = new StringBuilder
          var i = 0
          while (i < L) { sb.append(board(start + i)(c)); i += 1 }
          if (matchCells(sb.toString)) return true
        }
      }
      c += 1
    }
    false
  }
}
