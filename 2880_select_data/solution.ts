// LeetCode 2880 - Select Data
// https://leetcode.com/problems/select-data/

export function selectData(students: any[]): any[] {
    return students
        .filter((r) => r.student_id === 101 || r[0] === 101)
        .map((r) => (Array.isArray(r) ? { name: r[1], age: r[2] } : { name: r.name, age: r.age }));
}
