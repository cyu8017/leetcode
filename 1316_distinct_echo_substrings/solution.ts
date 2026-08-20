// LeetCode 1316 - Distinct Echo Substrings
// https://leetcode.com/problems/distinct-echo-substrings/

function distinctEchoSubstrings(text: string): number {
    const n = text.length;
    const mod1 = 1000000007, mod2 = 1000000009, base = 911382323;
    const h1 = Array(n + 1).fill(0), h2 = Array(n + 1).fill(0);
    const p1 = Array(n + 1).fill(1), p2 = Array(n + 1).fill(1);
    for (let i = 0; i < n; i++) {
        const code = text.charCodeAt(i);
        h1[i + 1] = (h1[i] * base + code) % mod1;
        h2[i + 1] = (h2[i] * base + code) % mod2;
        p1[i + 1] = (p1[i] * base) % mod1;
        p2[i + 1] = (p2[i] * base) % mod2;
    }
    const hashed = (left: any, right: any): any => {
        const length = right - left;
        return [
            ((h1[right] - h1[left] * p1[length]) % mod1 + mod1) % mod1,
            ((h2[right] - h2[left] * p2[length]) % mod2 + mod2) % mod2,
        ];
    };
    const echoes = new Set();
    for (let half = 1; half <= (n >> 1); half++) {
        for (let left = 0; left <= n - 2 * half; left++) {
            const a = hashed(left, left + half);
            const b = hashed(left + half, left + 2 * half);
            if (a[0] === b[0] && a[1] === b[1]) {
                const full = hashed(left, left + 2 * half);
                echoes.add(`${2 * half},${full[0]},${full[1]}`);
            }
        }
    }
    return echoes.size;
}
