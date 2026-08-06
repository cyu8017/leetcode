// LeetCode 1136 - Parallel Courses
// https://leetcode.com/problems/parallel-courses/

object Solution {
  def minimumSemesters(n: Int, relations: Array[Array[Int]]): Int = {
    val graph = Array.fill(n + 1)(scala.collection.mutable.ListBuffer.empty[Int])
    val indegree = Array.fill(n + 1)(0)
    for (e <- relations) {
      graph(e(0)) += e(1)
      indegree(e(1)) += 1
    }
    val q = scala.collection.mutable.Queue[Int]()
    for (i <- 1 to n if indegree(i) == 0) q.enqueue(i)
    var semesters = 0
    var taken = 0
    while (q.nonEmpty) {
      semesters += 1
      val size = q.size
      for (_ <- 0 until size) {
        val course = q.dequeue()
        taken += 1
        for (nxt <- graph(course)) {
          indegree(nxt) -= 1
          if (indegree(nxt) == 0) q.enqueue(nxt)
        }
      }
    }
    if (taken == n) semesters else -1
  }
}
