// LeetCode 1982 - Find Array Given Subset Sums
// https://leetcode.com/problems/find-array-given-subset-sums/

function recoverArray(n: number, sums: number[]): number[] {
    sums = sums.slice().sort((a, b: any) => a - b);
    const ans = [];
    for (let t = 0; t < n; t++) {
        const d = sums[1] - sums[0];
        const count = new Map();
        for (const x of sums) count.set(x, (count.get(x) || 0) + 1);
        const without = [], withD = [];
        for (const x of sums) {
            if ((count.get(x) || 0) === 0) continue;
            count.set(x, count.get(x) - 1);
            count.set(x + d, count.get(x + d) - 1);
            without.push(x);
            withD.push(x + d);
        }
        if (without.includes(0)) {
            ans.push(d);
            sums = without;
        } else {
            ans.push(-d);
            sums = withD;
        }
    }
    return ans;
}
