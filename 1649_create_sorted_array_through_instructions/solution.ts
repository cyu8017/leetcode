// LeetCode 1649 - Create Sorted Array through Instructions
// https://leetcode.com/problems/create-sorted-array-through-instructions/

function createSortedArray(instructions: number[]): number {
    const MOD = 1000000007;
    let mx = 0;
    for (const x of instructions) if (x > mx) mx = x;
    const size = mx + 2;
    const bit = Array(size + 1).fill(0);
    const query = (i: number): number => {
        let s = 0;
        while (i > 0) {
            s += bit[i];
            i -= i & -i;
        }
        return s;
    };
    let ans = 0;
    for (let i = 0; i < instructions.length; i++) {
        const x = instructions[i];
        ans = (ans + Math.min(query(x - 1), i - query(x))) % MOD;
        for (let j = x; j <= size; j += j & -j) bit[j]++;
    }
    return ans;
}
