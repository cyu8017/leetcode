// LeetCode 2693 - Call Function with Custom Context
// https://leetcode.com/problems/call-function-with-custom-context/

export function callPolyfill(self: Function, obj: any, ...args: any[]): any {
    const key = Symbol();
    obj[key] = self;
    const res = obj[key](...args);
    delete obj[key];
    return res;
}
