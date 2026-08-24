// LeetCode 3748 - Count Stable Subarrays
// https://leetcode.com/problems/count_stable_subarrays/

export function countStableSubarrays(nums: any, queries: any): any {
    const n = nums.length;
    const seg = [];
    const s = [0];
    let l = 0;
    for (let r = 0; r < n; r++) {
        if (r === n - 1 || nums[r] > nums[r + 1]) {
            seg.push(l);
            const k = r - l + 1;
            s.push(s[s.length - 1] + k * (k + 1) / 2);
            l = r + 1;
        }
    }
    const lowerBound = (a, x) => {
        let lo = 0, hi = a.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (a[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    const ans = new Array(queries.length);
    for (let idx = 0; idx < queries.length; idx++) {
        const left = queries[idx][0], right = queries[idx][1];
        const i = lowerBound(seg, left + 1);
        const j = lowerBound(seg, right + 1) - 1;
        if (i > j) {
            const k = right - left + 1;
            ans[idx] = k * (k + 1) / 2;
        } else {
            const a = seg[i] - left;
            const b = right - seg[j] + 1;
            ans[idx] = a * (a + 1) / 2 + s[j] - s[i] + b * (b + 1) / 2;
        }
    }
    return ans;
}
