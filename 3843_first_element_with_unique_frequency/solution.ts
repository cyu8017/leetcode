// LeetCode 3843 - First Element With Unique Frequency
// https://leetcode.com/problems/first-element-with-unique-frequency/

export function firstUniqueFreq(nums: any): any {
    const cnt = new Map();
    for (const x of nums) cnt.set(x, (cnt.get(x) || 0) + 1);
    const freq = new Map();
    for (const v of cnt.values()) freq.set(v, (freq.get(v) || 0) + 1);
    for (const x of nums) {
        if (freq.get(cnt.get(x)) === 1) return x;
    }
    return -1;
}
