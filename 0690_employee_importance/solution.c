// LeetCode 0690 - Employee Importance
// https://leetcode.com/problems/employee-importance/

struct Employee {
    int id;
    int importance;
    int* subordinates;
    int subordinatesSize;
};

static int dfs(struct Employee** employees, int employeesSize, int id) {
    for (int i = 0; i < employeesSize; i++) {
        if (employees[i]->id == id) {
            int total = employees[i]->importance;
            for (int j = 0; j < employees[i]->subordinatesSize; j++) {
                total += dfs(employees, employeesSize, employees[i]->subordinates[j]);
            }
            return total;
        }
    }
    return 0;
}

int getImportance(struct Employee** employees, int employeesSize, int id) {
    return dfs(employees, employeesSize, id);
}
