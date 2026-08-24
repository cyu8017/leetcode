// LeetCode 4012 - Count of Unfinished Tasks After Each Shift
// https://leetcode.com/problems/count-of-unfinished-tasks-after-each-shift/

object Solution {
  def countTasks(tasks: Array[Int], shifts: Array[Int]): Array[Int] = {
    val m = tasks.length
    val n = shifts.length
    val s = new Array[Long](m + 1)
    var i = 0
    while (i < m) {
      s(i + 1) = s(i) + tasks(i)
      i += 1
    }
    val ans = new Array[Int](n)
    var iIdx = 0
    var cur = 0L
    var j = 0
    while (j < n) {
      if (shifts(j).toLong < tasks(iIdx).toLong - cur) {
        cur += shifts(j)
        ans(j) = m - iIdx
      } else {
        val t = shifts(j).toLong - (tasks(iIdx).toLong - cur)
        if (t >= s(m) - s(iIdx + 1)) {
          iIdx = 0
          cur = 0
        } else {
          var l = iIdx + 1
          var r = m
          while (l < r) {
            val mid = (l + r) >> 1
            if (t < s(mid + 1) - s(iIdx + 1)) r = mid
            else l = mid + 1
          }
          cur = t - (s(l) - s(iIdx + 1))
          iIdx = l
          ans(j) = m - iIdx
        }
      }
      j += 1
    }
    ans
  }
}
