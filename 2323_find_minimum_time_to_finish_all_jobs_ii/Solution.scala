// LeetCode 2323 - Find Minimum Time to Finish All Jobs II
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs-ii/

object Solution {
  def minimumTime(jobs: Array[Int], workers: Array[Int]): Int = {
    java.util.Arrays.sort(jobs)
    java.util.Arrays.sort(workers)
    var ans = 0
    var i = 0
    while (i < jobs.length) {
      ans = math.max(ans, (jobs(i) + workers(i) - 1) / workers(i))
      i += 1
    }
    ans
  }
}
