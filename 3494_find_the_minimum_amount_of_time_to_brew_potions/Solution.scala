// LeetCode 3494 - Find the Minimum Amount of Time to Brew Potions
// https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

object Solution {
  def minTime(skill: Array[Int], mana: Array[Int]): Long = {
    val n = skill.length
    val m = mana.length
    val done = new Array[Long](n)
    var j = 0
    while (j < m) {
      var t = 0L
      var i = 0
      while (i < n) {
        if (done(i) > t) t = done(i)
        t += skill(i).toLong * mana(j)
        done(i) = t
        i += 1
      }
      i = n - 2
      while (i >= 0) {
        done(i) = done(i + 1) - skill(i + 1).toLong * mana(j)
        i -= 1
      }
      j += 1
    }
    done(n - 1)
  }
}
