// LeetCode 3036 - Number of Subarrays That Match a Pattern II
// https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/

export function countMatchingSubarrays(nums: any, pattern: any): any {
    const N = pattern.length;
    const ps = new Array(N + 1);
    ps[0] = -1;
    ps[1] = 0;
    for (let i = 2, p = 0; i <= N; i++) {
        const x = pattern[i - 1];
        while (p >= 0 && pattern[p] !== x) p = ps[p];
        p++;
        ps[i] = p;
    }
    let res = 0;
    const M = nums.length;
    for (let i = 1, p = 0; i < M; i++) {
        let t = nums[i] - nums[i - 1];
        if (t > 0) t = 1;
        else if (t < 0) t = -1;
        while (p >= 0 && pattern[p] !== t) p = ps[p];
        if (++p === N) {
            res++;
            p = ps[p];
        }
    }
    return res;
}
