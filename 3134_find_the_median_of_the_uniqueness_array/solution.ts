// LeetCode 3134 - Find the Median of the Uniqueness Array
// https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/

export function medianOfUniquenessArray(nums: number[]): number {
    const n = nums.length;
    const m = (1 + n) * n / 2;
    const check = (mx) => {
        const cnt = new Map();
        let l = 0, k = 0;
        for (let r = 0; r < n; r++) {
            cnt.set(nums[r], (cnt.get(nums[r]) || 0) + 1);
            while (cnt.size > mx) {
                const y = nums[l++];
                const nv = cnt.get(y) - 1;
                if (nv === 0) cnt.delete(y);
                else cnt.set(y, nv);
            }
            k += r - l + 1;
            if (k >= Math.floor((m + 1) / 2)) return true;
        }
        return false;
    };
    let lo = 1, hi = n;
    while (lo < hi) {
        const mid = lo + Math.floor((hi - lo) / 2);
        if (check(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
