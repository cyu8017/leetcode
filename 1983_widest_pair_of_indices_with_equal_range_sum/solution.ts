// LeetCode 1983 - Widest Pair of Indices With Equal Range Sum
// https://leetcode.com/problems/widest-pair-of-indices-with-equal-range-sum/

function widestPairOfIndices(nums1: number[], nums2: number[]): number {
    const first = new Map<number, number>([[0, -1]]);
    let ans = 0, s = 0;
    for (let i = 0; i < nums1.length; i++) {
        s += nums1[i] - nums2[i];
        if (first.has(s)) ans = Math.max(ans, i - first.get(s)!);
        else first.set(s, i);
    }
    return ans;
}
