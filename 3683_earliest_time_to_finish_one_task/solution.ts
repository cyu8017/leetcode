// LeetCode 3683 - Earliest Time to Finish One Task
// https://leetcode.com/problems/earliest-time-to-finish-one-task/

export function earliestTime(tasks: any): any {
    let ans = 200;
    for (const task of tasks) ans = Math.min(ans, task[0] + task[1]);
    return ans;
}
