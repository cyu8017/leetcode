// LeetCode 2963 - Count the Number of Good Partitions
// https://leetcode.com/problems/count-the-number-of-good-partitions/

export function numberOfGoodPartitions(nums: any): any {
    const mod = 1000000007;
    const last = new Map();
    for (let i = 0; i < nums.length; i++) last.set(nums[i], i);
    let ans = 1, end = 0;
    for (let i = 0; i < nums.length; i++) {
        if (last.get(nums[i]) > end) end = last.get(nums[i]);
        if (i === end && i !== nums.length - 1) ans = Number(BigInt(ans) * 2n % BigInt(mod));
    }
    return ans;
}
