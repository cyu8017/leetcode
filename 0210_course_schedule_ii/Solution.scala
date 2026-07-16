// LeetCode 0210 - Course Schedule II\n// https://leetcode.com/problems/\n\nimport scala.collection.mutable

object Solution {
  def findOrder(numCourses: Int, prerequisites: Array[Array[Int]]): Array[Int] = {
    val graph = Array.fill(numCourses)(mutable.ListBuffer[Int]())
    val indegree = Array.fill(numCourses)(0)
    for (pair <- prerequisites) { graph(pair(1)) += pair(0); indegree(pair(0)) += 1 }
    val queue = mutable.Queue[Int]()
    for (course <- 0 until numCourses if indegree(course) == 0) queue.enqueue(course)
    val order = Array.ofDim[Int](numCourses)
    var index = 0
    while (queue.nonEmpty) { val course = queue.dequeue(); order(index) = course; index += 1; for (next <- graph(course)) { indegree(next) -= 1; if (indegree(next) == 0) queue.enqueue(next) } }
    if (index == numCourses) order else Array.emptyIntArray
  }
}
