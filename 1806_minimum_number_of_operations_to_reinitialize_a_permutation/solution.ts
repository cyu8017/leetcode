// LeetCode 1806 - Minimum Number of Operations to Reinitialize a Permutation
// https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/

function reinitializePermutation(n: number): number {
    let perm = Array.from({ length: n }, (_, i) => i);
    const target = perm.slice();
    let operations = 0;
    while (true) {
        const newPerm = new Array<number>(n);
        for (let i = 0; i < n; i++) {
            if (i % 2 === 0) newPerm[i] = perm[i >> 1];
            else newPerm[i] = perm[(n >> 1) + ((i - 1) >> 1)];
        }
        perm = newPerm;
        operations += 1;
        if (perm.every((v, i) => v === target[i])) return operations;
    }
}
