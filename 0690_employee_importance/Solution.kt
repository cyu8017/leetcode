// LeetCode 0690 - Employee Importance
// https://leetcode.com/problems/employee-importance/

class Employee {
    var id: Int = 0
    var importance: Int = 0
    var subordinates: MutableList<Int> = ArrayList<Int>()
}

class Solution {
    private val table = HashMap<Int, Employee>()

    private fun dfs(eid: Int): Int {
        val emp = table[eid]!!
        var total = emp.importance
        for (sub in emp.subordinates) total += dfs(sub)
        return total
    }

    fun getImportance(employees: List<Employee>, id: Int): Int {
        table.clear()
        for (emp in employees) table[emp.id] = emp
        return dfs(id)
    }
}
