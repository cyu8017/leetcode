// LeetCode 2884 - Modify Columns
// https://leetcode.com/problems/modify-columns/

/**
 * @param {object[]} employees
 * @return {object[]}
 */
var modifySalaryColumn = function(employees) {
    return employees.map((r) => {
        if (Array.isArray(r)) return [r[0], r[1] * 2];
        return { ...r, salary: r.salary * 2 };
    });
};
