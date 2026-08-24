// LeetCode 2704 - To Be Or Not To Be
// https://leetcode.com/problems/to-be-or-not-to-be/

export function expect(val: any): any {
    return {
        toBe: function(other) {
            if (val === other) return true;
            throw new Error("Not Equal");
        },
        notToBe: function(other) {
            if (val !== other) return true;
            throw new Error("Equal");
        },
    };
}
