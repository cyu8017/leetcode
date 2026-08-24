// LeetCode 2638 - Count the Number of K-Free Subsets
// https://leetcode.com/problems/count-the-number-of-k-free-subsets/

export function countTheNumOfKFreeSubsets(nums: any, k: any): any {
    nums = nums.slice().sort((a, b) => a - b);
    const groups = new Map();
    for (const x of nums) {
        const key = x % k;
        if (!groups.has(key)) groups.set(key, []);
        groups.get(key).push(x);
    }
    let ans = 1;
    for (const g of groups.values()) {
        let prevVal = -1, prevTake = 0, prevSkip = 1;
        for (const v of g) {
            const skip = prevTake + prevSkip;
            const take = prevVal + k === v ? prevSkip : prevTake + prevSkip;
            prevTake = take;
            prevSkip = skip;
            prevVal = v;
        }
        ans *= prevTake + prevSkip;
    }
    return ans;
}
