// LeetCode 3659 - Partition Array Into K-Distinct Groups
// https://leetcode.com/problems/partition-array-into-k-distinct-groups/

export function partitionArray(nums: any, k: any): any {
    const n = nums.length;
    if (n % k !== 0) return false;
    const m = n / k;
    let mx = 0;
    for (const x of nums) mx = Math.max(mx, x);
    const cnt = new Array(mx + 1).fill(0);
    for (const x of nums)
        if (++cnt[x] > m) return false;
    return true;
}
