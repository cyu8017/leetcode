// LeetCode 2881 - Create a New Column
// https://leetcode.com/problems/create-a-new-column/

/**
 * @param {object[]} employees
 * @return {object[]}
 */
var createBonusColumn = function(employees) {
    return employees.map((r) => {
        if (Array.isArray(r)) return { name: r[0], salary: r[1], bonus: r[1] * 2 };
        return { ...r, bonus: r.salary * 2 };
    });
};
