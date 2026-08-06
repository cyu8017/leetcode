// LeetCode 1138 - Alphabet Board Path
// https://leetcode.com/problems/alphabet-board-path/

object Solution {
  def alphabetBoardPath(target: String): String = {
    var row = 0
    var col = 0
    val ans = new StringBuilder
    def moveTo(r: Int, c: Int): Unit = {
      while (row < r) { ans += 'D'; row += 1 }
      while (col > c) { ans += 'L'; col -= 1 }
      while (col < c) { ans += 'R'; col += 1 }
      while (row > r) { ans += 'U'; row -= 1 }
    }
    for (ch <- target) {
      val r = (ch - 'a') / 5
      val c = (ch - 'a') % 5
      if (r == 5) {
        while (col > 0) { ans += 'L'; col -= 1 }
        while (row < 5) { ans += 'D'; row += 1 }
      } else {
        moveTo(r, c)
      }
      ans += '!'
    }
    ans.toString
  }
}
