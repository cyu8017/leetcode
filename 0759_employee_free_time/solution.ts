// LeetCode 0759 - Employee Free Time
// https://leetcode.com/problems/employee-free-time/

export function employeeFreeTime(schedule: number[][][]): number[][] {
    const intervals = [];
    for (const employee of schedule)
        for (const item of employee)
            intervals.push([item[0], item[1]]);
    intervals.sort((a, b) => a[0] - b[0]);
    const merged = [];
    for (const iv of intervals) {
        if (merged.length === 0 || merged[merged.length - 1][1] < iv[0]) merged.push(iv);
        else merged[merged.length - 1][1] = Math.max(merged[merged.length - 1][1], iv[1]);
    }
    const result = [];
    for (let i = 1; i < merged.length; i++)
        result.push([merged[i - 1][1], merged[i][0]]);
    return result;
}
