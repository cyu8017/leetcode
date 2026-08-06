object Solution {
  def checkIfPrerequisite(numCourses: Int, prerequisites: Array[Array[Int]], queries: Array[Array[Int]]): List[Boolean] = {
    val reach = Array.fill(numCourses, numCourses)(false)
    prerequisites.foreach(edge => reach(edge(0))(edge(1)) = true)
    for (k <- 0 until numCourses; i <- 0 until numCourses if reach(i)(k); j <- 0 until numCourses) {
      reach(i)(j) = reach(i)(j) || reach(k)(j)
    }
    queries.map(query => reach(query(0))(query(1))).toList
  }
}
