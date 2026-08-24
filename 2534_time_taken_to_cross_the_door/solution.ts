// LeetCode 2534 - Time Taken to Cross the Door
// https://leetcode.com/problems/time-taken-to-cross-the-door/

export function timeTaken(arrival: number[], state: number[]): number[] {
    const n = arrival.length;
    const ans = new Array(n);
    const enter = [], exitq = [];
    let i = 0, t = 0, prev = 1;
    while (i < n || enter.length || exitq.length) {
        while (i < n && arrival[i] <= t) {
            if (state[i] === 0) enter.push(i);
            else exitq.push(i);
            i++;
        }
        if (!enter.length && !exitq.length) {
            if (i < n) {
                t = arrival[i];
                prev = 1;
            }
            continue;
        }
        if (prev === 1) {
            if (exitq.length) {
                ans[exitq.shift()] = t;
                prev = 1;
            } else {
                ans[enter.shift()] = t;
                prev = 0;
            }
        } else {
            if (enter.length) {
                ans[enter.shift()] = t;
                prev = 0;
            } else {
                ans[exitq.shift()] = t;
                prev = 1;
            }
        }
        t++;
    }
    return ans;
}
