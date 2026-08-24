// LeetCode 2881 - Create a New Column
// https://leetcode.com/problems/create-a-new-column/

export function createBonusColumn(employees: any[]): any[] {
    return employees.map((r) => {
        if (Array.isArray(r)) return { name: r[0], salary: r[1], bonus: r[1] * 2 };
        return { ...r, bonus: r.salary * 2 };
    });
}
