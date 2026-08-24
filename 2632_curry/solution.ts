// LeetCode 2632 - Curry
// https://leetcode.com/problems/curry/

export function curry(fn: any): any {
    return function curried(...args: any[]): any {
        if (args.length >= fn.length) return fn(...args);
        return function(...next) {
            return curried(...args, ...next);
        };
    };
}
