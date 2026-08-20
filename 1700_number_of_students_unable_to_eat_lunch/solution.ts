// LeetCode 1700 - Number of Students Unable to Eat Lunch
// https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

function countStudents(students: number[], sandwiches: number[]): number {
    const c = new Map();
    for (const x of students) c.set(x, (c.get(x) || 0) + 1);
    for (let i = 0; i < sandwiches.length; i++) {
        const x = sandwiches[i];
        if (!c.get(x)) return students.length - i;
        c.set(x, c.get(x) - 1);
    }
    return 0;
}
