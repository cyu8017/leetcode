// LeetCode 2406 - Divide Intervals Into Minimum Number of Groups
// https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

object Solution {
  def minGroups(intervals: Array[Array[Int]]): Int = {
    val events = Array.ofDim[Int](intervals.length * 2, 2)
    var idx = 0
    intervals.foreach { it =>
      events(idx) = Array(it(0), 1)
      idx += 1
      events(idx) = Array(it(1) + 1, -1)
      idx += 1
    }
    scala.util.Sorting.stableSort(events, (a: Array[Int], b: Array[Int]) => {
      if (a(0) != b(0)) a(0) < b(0) else a(1) < b(1)
    })
    var cur = 0
    var ans = 0
    events.foreach { e =>
      cur += e(1)
      ans = math.max(ans, cur)
    }
    ans
  }
}
