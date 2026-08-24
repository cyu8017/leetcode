// LeetCode 2432 - The Employee That Worked on the Longest Task
// https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

export function hardestWorker(n: number, logs: number[][]): number {
    let ans = logs[0][0], best = logs[0][1], prev = 0;
    for (const log of logs) {
        const dur = log[1] - prev;
        if (dur > best || (dur === best && log[0] < ans)) {
            best = dur;
            ans = log[0];
        }
        prev = log[1];
    }
    return ans;
}
