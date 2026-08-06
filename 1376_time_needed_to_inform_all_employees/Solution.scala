object Solution {
  def numOfMinutes(n: Int, headID: Int, manager: Array[Int], informTime: Array[Int]): Int = {
    val children = Array.fill(n)(collection.mutable.ArrayBuffer.empty[Int])
    manager.indices.filter(manager(_) != -1).foreach(i => children(manager(i)) += i)
    def dfs(employee: Int): Int = informTime(employee) + children(employee).map(dfs).foldLeft(0)(math.max)
    dfs(headID)
  }
}
