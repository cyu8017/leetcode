// LeetCode 3792 - Sum Of Increasing Product Blocks
// https://leetcode.com/problems/sum-of-increasing-product-blocks/

export function sumOfBlocks(n: any): any {
    const MOD = 1000000007;
    let ans = 0, k = 1;
    for (let i = 1; i <= n; i++) {
        let x = 1;
        for (let j = k; j < k + i; j++) x = Number(BigInt(x) * BigInt(j) % BigInt(MOD));
        ans = (ans + x) % MOD;
        k += i;
    }
    return ans;
}
