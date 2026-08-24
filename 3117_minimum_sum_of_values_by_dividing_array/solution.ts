// LeetCode 3117 - Minimum Sum of Values by Dividing Array
// https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

export function minimumValueSum(nums: number[], andValues: number[]): number {
    const INF = 1 << 29;
    const n = nums.length, m = andValues.length;
    const f = new Map();
    const dfs = (i, j, a) => {
        if (n - i < m - j) return INF;
        if (j === m) return i === n ? 0 : INF;
        a &= nums[i];
        if (a < andValues[j]) return INF;
        const key = (BigInt(i) << 36n) | (BigInt(j) << 32n) | BigInt(a >>> 0);
        const keyS = key.toString();
        if (f.has(keyS)) return f.get(keyS);
        let ans = dfs(i + 1, j, a);
        if (a === andValues[j]) {
            ans = Math.min(ans, dfs(i + 1, j + 1, -1) + nums[i]);
        }
        f.set(keyS, ans);
        return ans;
    };
    const ans = dfs(0, 0, -1);
    return ans < INF ? ans : -1;
}
