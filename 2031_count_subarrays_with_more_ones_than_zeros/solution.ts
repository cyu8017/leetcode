// LeetCode 2031 - Count Subarrays With More Ones Than Zeros
// https://leetcode.com/problems/count-subarrays-with-more-ones-than-zeros/

export function subarraysWithMoreZerosThanOnes(nums: number[]): number {
    const MOD = 1000000007;
    class Fenwick {
        constructor(n) { this.bit = new Array(n + 2).fill(0); }
        add(i, v) { for (; i < this.bit.length; i += i & -i) this.bit[i] += v; }
        sum(i) { let s = 0; for (; i > 0; i -= i & -i) s += this.bit[i]; return s; }
    }
    const n = nums.length, offset = n + 1;
    const fw = new Fenwick(2 * n + 5);
    let pref = 0, ans = 0;
    fw.add(offset, 1);
    for (const x of nums) {
        pref += (x === 1) ? 1 : -1;
        const idx = pref + offset;
        ans = (ans + fw.sum(idx - 1)) % MOD;
        fw.add(idx, 1);
    }
    return ans;
}
