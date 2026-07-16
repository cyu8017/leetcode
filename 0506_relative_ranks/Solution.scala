// LeetCode 0506 - Relative Ranks
// https://leetcode.com/problems/relative-ranks/

object Solution {
  private val medals = Map(
    1 -> "Gold Medal",
    2 -> "Silver Medal",
    3 -> "Bronze Medal",
  )

  def findRelativeRanks(score: Array[Int]): Array[String] = {
    val order = score.indices.sortBy(index => -score(index))
    val result = Array.fill(score.length)("")
    order.zipWithIndex.foreach { case (index, rank) =>
      result(index) = medals.getOrElse(rank + 1, (rank + 1).toString)
    }
    result
  }
}
