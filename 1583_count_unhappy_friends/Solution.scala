// LeetCode 1583 - Count Unhappy Friends
// https://leetcode.com/problems/count-unhappy-friends/

object Solution {
  def unhappyFriends(n: Int, preferences: Array[Array[Int]], pairs: Array[Array[Int]]): Int = {
    val rank = preferences.map(pref => pref.zipWithIndex.map { case (friend, i) => friend -> i }.toMap)
    val partner = Array.fill(n)(0)
    for (Array(a, b) <- pairs) {
      partner(a) = b
      partner(b) = a
    }
    var unhappy = 0
    for (x <- 0 until n) {
      val y = partner(x)
      val better = preferences(x).take(rank(x)(y))
      if (better.exists(u => rank(u)(x) < rank(u)(partner(u)))) unhappy += 1
    }
    unhappy
  }
}
