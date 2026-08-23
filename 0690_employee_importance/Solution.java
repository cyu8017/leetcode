// LeetCode 0690 - Employee Importance
// https://leetcode.com/problems/employee-importance/

import java.util.*;

class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;
}

class Solution {
    private Map<Integer, Employee> table = new HashMap<>();

    private int dfs(int eid) {
        Employee emp = table.get(eid);
        int total = emp.importance;
        for (int sub : emp.subordinates) total += dfs(sub);
        return total;
    }

    public int getImportance(List<Employee> employees, int id) {
        table.clear();
        for (Employee emp : employees) table.put(emp.id, emp);
        return dfs(id);
    }
}
