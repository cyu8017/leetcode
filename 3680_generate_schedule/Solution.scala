// LeetCode 3680 - Generate Schedule
// https://leetcode.com/problems/generate-schedule/

object Solution {
  def generateSchedule(n: Int): Array[Array[Int]] = {
    if (n < 5) return Array.empty[Array[Int]]
    val matches = new java.util.ArrayList[Array[Int]]()
    var i = 0
    while (i < n) {
      var j = 0
      while (j < n) {
        if (i != j) matches.add(Array(i, j))
        j += 1
      }
      i += 1
    }
    val used = Array.fill(matches.size())(false)
    val sched = new java.util.ArrayList[Array[Int]]()
    var last0 = -1
    var last1 = -1

    def dfs(): Boolean = {
      if (sched.size() == matches.size()) return true
      var ii = 0
      while (ii < matches.size()) {
        if (!used(ii)) {
          val m = matches.get(ii)
          if (!(m(0) == last0 || m(0) == last1 || m(1) == last0 || m(1) == last1)) {
            used(ii) = true
            sched.add(m)
            val p0 = last0
            val p1 = last1
            last0 = m(0)
            last1 = m(1)
            if (dfs()) return true
            last0 = p0
            last1 = p1
            sched.remove(sched.size() - 1)
            used(ii) = false
          }
        }
        ii += 1
      }
      false
    }

    if (dfs()) {
      val res = new Array[Array[Int]](sched.size())
      i = 0
      while (i < sched.size()) {
        res(i) = sched.get(i)
        i += 1
      }
      res
    } else Array.empty[Array[Int]]
  }
}
