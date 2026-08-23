// LeetCode 0690 - Employee Importance
// https://leetcode.com/problems/employee-importance/

using System.Collections.Generic;

public class Employee {
    public int id;
    public int importance;
    public IList<int> subordinates;
}

public class Solution {
    private Dictionary<int, Employee> table = new Dictionary<int, Employee>();

    private int Dfs(int eid) {
        Employee emp = table[eid];
        int total = emp.importance;
        foreach (int sub in emp.subordinates) total += Dfs(sub);
        return total;
    }

    public int GetImportance(IList<Employee> employees, int id) {
        table.Clear();
        foreach (Employee emp in employees) table[emp.id] = emp;
        return Dfs(id);
    }
}
