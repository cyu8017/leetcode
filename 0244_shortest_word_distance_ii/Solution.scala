// LeetCode 0244 - Shortest Word Distance II
// https://leetcode.com/problems/shortest-word-distance-ii/

class WordDistance(wordsDict: Array[String]) {
  private val positions = scala.collection.mutable.Map.empty[String, List[Int]].withDefaultValue(Nil)

  wordsDict.zipWithIndex.foreach { case (word, index) =>
    positions.update(word, positions(word) :+ index)
  }

  def shortest(word1: String, word2: String): Int = {
    val left = positions(word1)
    val right = positions(word2)
    var i = 0
    var j = 0
    var best = Int.MaxValue
    while (i < left.length && j < right.length) {
      best = math.min(best, math.abs(left(i) - right(j)))
      if (left(i) <= right(j)) i += 1 else j += 1
    }
    best
  }
}
