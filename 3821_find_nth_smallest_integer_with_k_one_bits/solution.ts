// LeetCode 3821 - Find Nth Smallest Integer With K One Bits
// https://leetcode.com/problems/find_nth_smallest_integer_with_k_one_bits/

export function nthSmallest(n: any, k: any): any {
    const MX = 50;
    const C = Array.from({length: MX}, () => new Array(MX + 1).fill(0n));
    for (let i = 0; i < MX; i++) {
        C[i][0] = 1n;
        for (let j = 1; j <= i; j++) C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
    }
    let ans = 0n;
    let nn = BigInt(n);
    for (let i = 49; i >= 0; i--) {
        if (k >= 0 && nn > C[i][k]) {
            nn -= C[i][k];
            ans |= 1n << BigInt(i);
            k--;
            if (k === 0) break;
        }
    }
    return Number(ans);
}
