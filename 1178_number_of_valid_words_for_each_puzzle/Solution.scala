// LeetCode 1178 - Number of Valid Words for Each Puzzle
// https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

object Solution {
  def findNumOfValidWords(words: Array[String], puzzles: Array[String]): Array[Int] = {
    def maskOf(s: String): Int = {
      var mask = 0
      for (ch <- s) mask |= 1 << (ch - 'a')
      mask
    }
    val freq = scala.collection.mutable.Map.empty[Int, Int]
    for (w <- words) {
      val m = maskOf(w)
      freq(m) = freq.getOrElse(m, 0) + 1
    }
    puzzles.map { puzzle =>
      val first = 1 << (puzzle(0) - 'a')
      val full = maskOf(puzzle)
      var sub = full
      var total = 0
      var done = false
      while (!done) {
        if ((sub & first) != 0) total += freq.getOrElse(sub, 0)
        if (sub == 0) done = true
        else sub = (sub - 1) & full
      }
      total
    }
  }
}
