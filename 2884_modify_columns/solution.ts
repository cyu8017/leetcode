// LeetCode 2884 - Modify Columns
// https://leetcode.com/problems/modify-columns/

export function modifySalaryColumn(employees: any[]): any[] {
    return employees.map((r) => {
        if (Array.isArray(r)) return [r[0], r[1] * 2];
        return { ...r, salary: r.salary * 2 };
    });
}
