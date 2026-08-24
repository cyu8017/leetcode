// LeetCode 0825 - Friends Of Appropriate Ages
// https://leetcode.com/problems/friends-of-appropriate-ages/

object Solution {
  def numFriendRequests(ages: Array[Int]): Int = {
    val count = Array.ofDim[Int](121)
    ages.foreach(age => count(age) += 1)
    var ans = 0
    var x = 1
    while (x <= 120) {
      if (count(x) != 0) {
        var y = 1
        while (y <= 120) {
          if (count(y) != 0) {
            if (!(y <= 0.5 * x + 7 || y > x || (y > 100 && x < 100))) {
              ans += count(x) * count(y)
              if (x == y) ans -= count(x)
            }
          }
          y += 1
        }
      }
      x += 1
    }
    ans
  }
}
