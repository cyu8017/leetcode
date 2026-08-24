// LeetCode 2449 - Minimum Number of Operations to Make Arrays Similar
// https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

export function makeSimilar(nums: number[], target: number[]): number {
    nums.sort((a, b) => a - b);
    target.sort((a, b) => a - b);
    const oddN = [], evenN = [], oddT = [], evenT = [];
    for (const x of nums) (x % 2 === 0 ? evenN : oddN).push(x);
    for (const x of target) (x % 2 === 0 ? evenT : oddT).push(x);
    let ans = 0;
    for (let i = 0; i < oddN.length; i++) {
        const diff = oddN[i] - oddT[i];
        if (diff > 0) ans += Math.floor(diff / 2);
    }
    for (let i = 0; i < evenN.length; i++) {
        const diff = evenN[i] - evenT[i];
        if (diff > 0) ans += Math.floor(diff / 2);
    }
    return ans;
}
