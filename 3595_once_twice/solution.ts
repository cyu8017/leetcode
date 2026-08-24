// LeetCode 3595 - Once Twice
// https://leetcode.com/problems/once-twice/

export function onceTwice(nums: any): any {
    const freq = new Map();
    for (const x of nums) freq.set(x, (freq.get(x) || 0) + 1);
    let a = 0, b = 0;
    for (const [k, v] of freq) {
        if (v === 1) a = k;
        else if (v === 2) b = k;
    }
    return [a, b];
}
