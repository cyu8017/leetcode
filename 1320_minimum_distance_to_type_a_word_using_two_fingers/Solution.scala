// LeetCode 1320 - Minimum Distance to Type a Word Using Two Fingers
// https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/

object Solution {
  def minimumDistance(word: String): Int = {
    def distance(a: Int, b: Int): Int = {
      if (a == 26) 0
      else math.abs(a / 6 - b / 6) + math.abs(a % 6 - b % 6)
    }
    val letters = word.map(_ - 'A')
    var dp = scala.collection.mutable.HashMap(26 -> 0)
    var previous = letters.head
    for (current <- letters.tail) {
      val nxt = scala.collection.mutable.HashMap[Int, Int]()
      for ((free, cost) <- dp) {
        nxt(free) = math.min(nxt.getOrElse(free, Int.MaxValue / 2), cost + distance(previous, current))
        nxt(previous) = math.min(nxt.getOrElse(previous, Int.MaxValue / 2), cost + distance(free, current))
      }
      dp = nxt
      previous = current
    }
    dp.values.min
  }
}
