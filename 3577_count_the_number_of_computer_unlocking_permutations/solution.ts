// LeetCode 3577 - Count the Number of Computer Unlocking Permutations
// https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

export function countPermutations(complexity: any): any {
    const mod = 1000000007n;
    let ans = 1n;
    for (let i = 1; i < complexity.length; i++) {
        if (complexity[i] <= complexity[0]) return 0;
        ans = ans * BigInt(i) % mod;
    }
    return Number(ans);
}
