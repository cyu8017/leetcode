// LeetCode 2868 - The Wording Game
// https://leetcode.com/problems/the-wording-game/

object Solution {
  def canAliceWin(a: Array[String], b: Array[String]): Boolean = {
    var i = 0
    var j = 0
    var last: Char = 0
    var alice = true
    while (true) {
      if (alice) {
        while (i < a.length && a(i).charAt(0) <= last) i += 1
        if (i == a.length) return false
        last = a(i).charAt(a(i).length - 1)
        i += 1
      } else {
        while (j < b.length && b(j).charAt(0) <= last) j += 1
        if (j == b.length) return true
        last = b(j).charAt(b(j).length - 1)
        j += 1
      }
      alice = !alice
    }
    false
  }
}
