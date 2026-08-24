// LeetCode 0646 - Maximum Length of Pair Chain
// https://leetcode.com/problems/maximum-length-of-pair-chain/

export function findLongestChain(pairs: number[][]): number {
    pairs.sort((a, b) => a[1] - b[1]);
    let length = 0, currentEnd = -Infinity;
    for (const pair of pairs) {
        if (pair[0] > currentEnd) {
            ++length;
            currentEnd = pair[1];
        }
    }
    return length;
}
