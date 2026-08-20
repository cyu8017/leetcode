// LeetCode 1244 - Design A Leaderboard
// https://leetcode.com/problems/design-a-leaderboard/

class Leaderboard() {
  private val scores = scala.collection.mutable.Map.empty[Int, Int].withDefaultValue(0)

  def addScore(playerId: Int, score: Int): Unit = {
    scores(playerId) += score
  }

  def top(K: Int): Int =
    scores.values.toSeq.sorted(Ordering[Int].reverse).take(K).sum

  def reset(playerId: Int): Unit = {
    scores.remove(playerId)
  }
}
