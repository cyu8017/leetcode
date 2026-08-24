// LeetCode 2619 - Array Prototype Last
// https://leetcode.com/problems/array-prototype-last/

export function last(self: any[]): null | boolean | number | string | any[] | any {
    if (self.length === 0) return -1;
    return self[self.length - 1];
}
