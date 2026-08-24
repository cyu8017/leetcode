// LeetCode 2804 - Array Prototype ForEach
// https://leetcode.com/problems/array-prototype-foreach/

export function forEach(self: any[], callback: Function, context: any): void {
    for (let i = 0; i < self.length; i++) {
        callback.call(context, self[i], i, self);
    }
}
