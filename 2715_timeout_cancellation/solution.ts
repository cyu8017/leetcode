// LeetCode 2715 - Timeout Cancellation
// https://leetcode.com/problems/timeout-cancellation/

export function cancellable(fn: any, args: any, t: any): any {
    const timer = setTimeout(() => fn(...args), t);
    return function() { clearTimeout(timer); };
}
