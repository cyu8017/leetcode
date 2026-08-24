// LeetCode 2391 - Minimum Amount of Time to Collect Garbage
// https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

object Solution {
  def garbageCollection(garbage: Array[String], travel: Array[Int]): Int = {
    var ans = 0
    var lastM = 0
    var lastP = 0
    var lastG = 0
    var i = 0
    while (i < garbage.length) {
      ans += garbage(i).length
      var j = 0
      while (j < garbage(i).length) {
        val c = garbage(i).charAt(j)
        if (c == 'M') lastM = i
        else if (c == 'P') lastP = i
        else lastG = i
        j += 1
      }
      i += 1
    }
    val pref = Array.fill(travel.length + 1)(0)
    i = 0
    while (i < travel.length) {
      pref(i + 1) = pref(i) + travel(i)
      i += 1
    }
    ans + pref(lastM) + pref(lastP) + pref(lastG)
  }
}
