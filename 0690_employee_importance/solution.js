// LeetCode 0690 - Employee Importance
// https://leetcode.com/problems/employee-importance/

/**
 * @param {Employee[]} employees
 * @param {number} id
 * @return {number}
 */
var getImportance = function(employees, id) {
    const table = new Map();
    for (const emp of employees) table.set(emp.id, emp);
    const dfs = (eid) => {
        const emp = table.get(eid);
        let total = emp.importance;
        for (const sub of emp.subordinates) total += dfs(sub);
        return total;
    };
    return dfs(id);
};
