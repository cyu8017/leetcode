// LeetCode 0690 - Employee Importance
// https://leetcode.com/problems/employee-importance/

class Employee(var id: Int = 0, var importance: Int = 0, var subordinates: List[Int] = Nil)

object Solution {
  def getImportance(employees: List[Employee], id: Int): Int = {
    val table = scala.collection.mutable.HashMap.empty[Int, Employee]
    for (emp <- employees) table(emp.id) = emp
    def dfs(eid: Int): Int = {
      val emp = table(eid)
      var total = emp.importance
      for (sub <- emp.subordinates) total += dfs(sub)
      total
    }
    dfs(id)
  }
}
