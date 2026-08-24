// LeetCode 2883 - Drop Missing Data
// https://leetcode.com/problems/drop-missing-data/

export function dropMissingData(students: any[]): any[] {
    return students.filter((r) => {
        const name = Array.isArray(r) ? r[1] : r.name;
        return name !== null && name !== undefined && name !== '';
    });
}
