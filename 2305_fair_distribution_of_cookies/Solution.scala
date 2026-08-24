// LeetCode 2305 - Fair Distribution of Cookies
// https://leetcode.com/problems/fair-distribution-of-cookies/

object Solution {
  def distributeCookies(cookies: Array[Int], k: Int): Int = {
    val bags = Array.fill(k)(0)
    var ans = Int.MaxValue

    def dfs(i: Int): Unit = {
      if (i == cookies.length) {
        var mx = 0
        bags.foreach(b => mx = math.max(mx, b))
        ans = math.min(ans, mx)
        return
      }
      val seen = scala.collection.mutable.HashSet.empty[Int]
      var j = 0
      var stop = false
      while (j < bags.length && !stop) {
        if (seen.add(bags(j))) {
          bags(j) += cookies(i)
          if (bags(j) < ans) dfs(i + 1)
          bags(j) -= cookies(i)
          if (bags(j) == 0) stop = true
        }
        j += 1
      }
    }

    dfs(0)
    ans
  }
}
