// LeetCode 2886 - Change Data Type
// https://leetcode.com/problems/change-data-type/

export function changeDatatype(students: any[]): any[] {
    return students.map((r) => {
        if (Array.isArray(r)) return [r[0], r[1], r[2], Math.trunc(r[3])];
        return { ...r, grade: Math.trunc(r.grade) };
    });
}
