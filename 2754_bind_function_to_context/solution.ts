// LeetCode 2754 - Bind Function to Context
// https://leetcode.com/problems/bind-function-to-context/

export function bindPolyfill(self: Function, obj: any): Function {
    const fn = self;
    return function(...args) {
        return fn.apply(obj, args);
    };
}
