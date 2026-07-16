// LeetCode 0207 - Course Schedule\n// https://leetcode.com/problems/\n\nimport scala.collection.mutable

object Solution {
  def canFinish(numCourses: Int, prerequisites: Array[Array[Int]]): Boolean = {
    val graph = Array.fill(numCourses)(mutable.ListBuffer[Int]())
    val indegree = Array.fill(numCourses)(0)
    for (pair <- prerequisites) { graph(pair(1)) += pair(0); indegree(pair(0)) += 1 }
    val queue = mutable.Queue[Int]()
    for (course <- 0 until numCourses if indegree(course) == 0) queue.enqueue(course)
    var taken = 0
    while (queue.nonEmpty) { val course = queue.dequeue(); taken += 1; for (next <- graph(course)) { indegree(next) -= 1; if (indegree(next) == 0) queue.enqueue(next) } }
    taken == numCourses
  }
}
