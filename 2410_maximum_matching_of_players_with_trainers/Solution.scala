// LeetCode 2410 - Maximum Matching of Players With Trainers
// https://leetcode.com/problems/maximum-matching-of-players-with-trainers/

object Solution {
  def matchPlayersAndTrainers(players: Array[Int], trainers: Array[Int]): Int = {
    java.util.Arrays.sort(players)
    java.util.Arrays.sort(trainers)
    var i = 0
    var j = 0
    var ans = 0
    while (i < players.length && j < trainers.length) {
      if (players(i) <= trainers(j)) {
        ans += 1
        i += 1
        j += 1
      } else j += 1
    }
    ans
  }
}
