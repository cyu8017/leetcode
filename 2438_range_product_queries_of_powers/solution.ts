// LeetCode 2438 - Range Product Queries of Powers
// https://leetcode.com/problems/range-product-queries-of-powers/

export function productQueries(n: number, queries: number[][]): number[] {
    const mod = 1000000007;
    const powers = [];
    for (let bit = 0; bit < 31; bit++) {
        if (((n >> bit) & 1) !== 0) powers.push(1 << bit);
    }
    const ans = Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        let prod = 1;
        for (let j = queries[i][0]; j <= queries[i][1]; j++)
            prod = (prod * powers[j]) % mod;
        ans[i] = prod;
    }
    return ans;
}
