// LeetCode 2695 - Array Wrapper
// https://leetcode.com/problems/array-wrapper/

export class ArrayWrapper {
    constructor(nums: any) {
    this.nums = nums;
}
    valueOf(): any {
    let s = 0;
    for (const x of this.nums) s += x;
    return s;
}
    toString(): any {
    return "[" + this.nums.join(",") + "]";
}
}
