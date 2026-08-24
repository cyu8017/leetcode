// LeetCode 3215 - Count Triplets with Even XOR Set Bits II
// https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-ii/

export function tripletCount(a: any, b: any, c: any): any {
    const bitCount = (x) => { let n = 0; while (x) { n += x & 1; x >>>= 1; } return n; };
    const cnt1 = [0, 0], cnt2 = [0, 0], cnt3 = [0, 0];
    for (const x of a) cnt1[bitCount(x) % 2]++;
    for (const x of b) cnt2[bitCount(x) % 2]++;
    for (const x of c) cnt3[bitCount(x) % 2]++;
    let ans = 0;
    for (let i = 0; i < 2; i++)
        for (let j = 0; j < 2; j++)
            for (let k = 0; k < 2; k++)
                if ((i + j + k) % 2 === 0) ans += cnt1[i] * cnt2[j] * cnt3[k];
    return ans;
}
