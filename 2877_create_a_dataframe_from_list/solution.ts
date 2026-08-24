// LeetCode 2877 - Create a DataFrame from List
// https://leetcode.com/problems/create-a-dataframe-from-list/

export function createDataframe(studentData: number[][]): any[] {
    return studentData.map(([student_id, age]) => ({ student_id, age }));
}
