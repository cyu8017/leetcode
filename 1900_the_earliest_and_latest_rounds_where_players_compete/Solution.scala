// LeetCode 1900 - The Earliest and Latest Rounds Where Players Compete
// https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

import scala.collection.mutable

object Solution {
  def earliestAndLatest(n: Int, firstPlayer: Int, secondPlayer: Int): Array[Int] = {
    val first = firstPlayer
    val second = secondPlayer
    val memo = mutable.Map.empty[List[Int], Array[Int]]

    def dfs(players: List[Int]): Array[Int] = {
      memo.get(players) match {
        case Some(cached) => return cached
        case None =>
      }
      val count = players.length
      val firstIndex = players.indexOf(first)
      val secondIndex = players.indexOf(second)
      if (firstIndex + secondIndex == count - 1) {
        val result = Array(1, 1)
        memo(players) = result
        return result
      }

      val choices = mutable.ArrayBuffer.empty[List[Int]]
      for (index <- 0 until count / 2) {
        val left = players(index)
        val right = players(count - 1 - index)
        if (left == first || left == second) choices += List(left)
        else if (right == first || right == second) choices += List(right)
        else choices += List(left, right)
      }
      if (count % 2 == 1) choices += List(players(count / 2))

      var earliest = Int.MaxValue / 2
      var latest = 0

      def explore(i: Int, picks: mutable.ArrayBuffer[Int]): Unit = {
        if (i == choices.length) {
          val winners = picks.sorted.toList
          val Array(early, late) = dfs(winners)
          earliest = math.min(earliest, early + 1)
          latest = math.max(latest, late + 1)
          return
        }
        for (pick <- choices(i)) {
          picks += pick
          explore(i + 1, picks)
          picks.remove(picks.length - 1)
        }
      }

      explore(0, mutable.ArrayBuffer.empty[Int])
      val result = Array(earliest, latest)
      memo(players) = result
      result
    }

    dfs((1 to n).toList)
  }
}
