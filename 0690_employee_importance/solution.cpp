// LeetCode 0690 - Employee Importance
// https://leetcode.com/problems/employee-importance/

#include <unordered_map>
#include <vector>

class Employee {
public:
    int id;
    int importance;
    std::vector<int> subordinates;
};

class Solution {
    std::unordered_map<int, Employee*> table_;

    int dfs(int eid) {
        Employee* emp = table_[eid];
        int total = emp->importance;
        for (int sub : emp->subordinates) {
            total += dfs(sub);
        }
        return total;
    }

public:
    int getImportance(std::vector<Employee*> employees, int id) {
        table_.clear();
        for (Employee* emp : employees) {
            table_[emp->id] = emp;
        }
        return dfs(id);
    }
};
