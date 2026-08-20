// LeetCode 1331 - Rank Transform Of An Array
// https://leetcode.com/problems/rank-transform-of-an-array/

function arrayRankTransform(arr: number[]): number[] {
    const sorted = [...new Set(arr)].sort((a, b: any): any => a - b);
    const rank = new Map(sorted.map((value, i: any): any => [value, i + 1]));
    return arr.map((value: any): any => rank.get(value));
}
