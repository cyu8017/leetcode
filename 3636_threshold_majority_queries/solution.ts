// LeetCode 3636 - Threshold Majority Queries
// https://leetcode.com/problems/threshold-majority-queries/

export function subarrayMajority(nums: any, queries: any): any {
    const ans = new Array(queries.length);
    for (let qi = 0; qi < queries.length; qi++) {
        const l = queries[qi][0], r = queries[qi][1], t = queries[qi][2];
        const cnt = new Map();
        for (let i = l; i <= r; i++) cnt.set(nums[i], (cnt.get(nums[i]) || 0) + 1);
        let best = -1, bestC = 0;
        for (const [v, c] of cnt) {
            if (c >= t && (c > bestC || (c === bestC && (best === -1 || v < best)))) {
                bestC = c;
                best = v;
            }
        }
        ans[qi] = best;
    }
    return ans;
}
