// LeetCode 3424 - Minimum Cost to Make Arrays Identical
// https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/

export function minCost(arr: any, brr: any, k: any): any {
    let noSwap = 0;
    for (let i = 0; i < arr.length; i++) noSwap += Math.abs(arr[i] - brr[i]);
    const a2 = arr.slice().sort((a, b) => a - b);
    const b2 = brr.slice().sort((a, b) => a - b);
    let withSwap = k;
    for (let i = 0; i < a2.length; i++) withSwap += Math.abs(a2[i] - b2[i]);
    return noSwap < withSwap ? noSwap : withSwap;
}
