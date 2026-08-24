// LeetCode 2725 - Interval Cancellation
// https://leetcode.com/problems/interval-cancellation/

export function cancellable(fn: any, args: any, t: any): any {
    fn(...args);
    const id = setInterval(() => fn(...args), t);
    return function() { clearInterval(id); };
}
