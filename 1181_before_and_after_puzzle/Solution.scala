// LeetCode 1181 - Before and After Puzzle
// https://leetcode.com/problems/before-and-after-puzzle/

object Solution {
  def beforeAndAfterPuzzles(phrases: Array[String]): List[String] = {
    val split = phrases.map(_.split(" ").toSeq)
    val result = scala.collection.mutable.Set.empty[String]
    for (i <- split.indices; j <- split.indices if i != j) {
      if (split(i).last == split(j).head) {
        result += (split(i) ++ split(j).tail).mkString(" ")
      }
    }
    result.toList.sorted
  }
}
