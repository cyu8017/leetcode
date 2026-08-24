// LeetCode 2637 - Promise Time Limit
// https://leetcode.com/problems/promise-time-limit/

export function timeLimit(fn: any, t: any): any {
    return async function(...args) {
        return await Promise.race([
            fn(...args),
            new Promise((_, reject) => setTimeout(() => reject("Time Limit Exceeded"), t)),
        ]);
    };
}
