// LeetCode 1733 - Minimum Number of People to Teach
// https://leetcode.com/problems/minimum-number-of-people-to-teach/

object Solution {
  def minimumTeachings(n: Int, languages: Array[Array[Int]], friendships: Array[Array[Int]]): Int = {
    val users = languages.length
    val knows = Array.ofDim[Boolean](users, n + 1)
    for (user <- 0 until users; lang <- languages(user)) {
      knows(user)(lang) = true
    }
    val need = scala.collection.mutable.Set.empty[Int]
    for (friendship <- friendships) {
      val u = friendship(0) - 1
      val v = friendship(1) - 1
      val shares = languages(u).exists(lang => knows(v)(lang))
      if (!shares) {
        need += u
        need += v
      }
    }
    if (need.isEmpty) {
      0
    } else {
      (1 to n).map(lang => need.count(user => !knows(user)(lang))).min
    }
  }
}
