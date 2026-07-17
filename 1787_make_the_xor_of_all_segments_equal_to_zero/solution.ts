// LeetCode 1787 - Make the XOR of All Segments Equal to Zero
// https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/

function minChanges(nums: number[], k: number): number {
    const freq: Map<number, number>[] = Array.from({ length: k }, () => new Map());
    const size = new Array(k).fill(0);
    for (let i = 0; i < nums.length; i++) {
        const g = i % k;
        freq[g].set(nums[i], (freq[g].get(nums[i]) || 0) + 1);
        size[g]++;
    }
    const INF = 1000000000;
    let dp = new Array(256).fill(INF);
    dp[0] = 0;
    for (let i = 0; i < k; i++) {
        const ndp = new Array(256).fill(INF);
        for (let xv = 0; xv < 256; xv++) {
            const cost = size[i] - (freq[i].get(xv) || 0);
            for (let xo = 0; xo < 256; xo++) {
                if (dp[xo] === INF) continue;
                const key = xo ^ xv;
                if (dp[xo] + cost < ndp[key]) {
                    ndp[key] = dp[xo] + cost;
                }
            }
        }
        dp = ndp;
    }
    return dp[0];
}
