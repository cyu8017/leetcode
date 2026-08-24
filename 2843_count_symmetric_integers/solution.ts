// LeetCode 2843 - Count Symmetric Integers
// https://leetcode.com/problems/count-symmetric-integers/

export function countSymmetricIntegers(low: number, high: number): number {
    let ans = 0;
    for (let x = low; x <= high; x++) {
        const s = String(x);
        if (s.length % 2 !== 0) continue;
        const mid = s.length / 2;
        let a = 0, b = 0;
        for (let i = 0; i < mid; i++) {
            a += s.charCodeAt(i) - 48;
            b += s.charCodeAt(mid + i) - 48;
        }
        if (a === b) ans++;
    }
    return ans;
}
