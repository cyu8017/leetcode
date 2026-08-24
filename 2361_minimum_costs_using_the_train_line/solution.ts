// LeetCode 2361 - Minimum Costs Using the Train Line
// https://leetcode.com/problems/minimum-costs-using-the-train-line/

export function minimumCosts(regular: number[], express: number[], expressCost: number): number[] {
    const n = regular.length;
    const ans = Array(n);
    let reg = 0, exp = expressCost;
    for (let i = 0; i < n; i++) {
        const nextReg = Math.min(reg + regular[i], exp + express[i]);
        const nextExp = Math.min(reg + regular[i] + expressCost, exp + express[i]);
        reg = nextReg;
        exp = nextExp;
        ans[i] = Math.min(reg, exp);
    }
    return ans;
}
