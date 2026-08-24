// LeetCode 3755 - Find Maximum Balanced Xor Subarray Length
// https://leetcode.com/problems/find_maximum_balanced_xor_subarray_length/

export function maxBalancedSubarray(nums: any): any {
    const d = new Map();
    let a = 0, b = nums.length, ans = 0;
    d.set(BigInt(b), -1);
    for (let i = 0; i < nums.length; i++) {
        a ^= nums[i];
        if (nums[i] % 2 === 0) b++;
        else b--;
        const key = (BigInt(a) << 32n) | (BigInt(b) & 0xffffffffn);
        if (d.has(key)) ans = Math.max(ans, i - d.get(key));
        else d.set(key, i);
    }
    return ans;
}
