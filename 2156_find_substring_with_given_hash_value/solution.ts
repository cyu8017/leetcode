// LeetCode 2156 - Find Substring With Given Hash Value
// https://leetcode.com/problems/find-substring-with-given-hash-value/

export function subStrHash(s: string, power: number, modulo: number, k: number, hashValue: number): string {
    const n = s.length;
    let pk = 1;
    for (let i = 0; i < k - 1; i++) pk = pk * power % modulo;
    let h = 0;
    let ans = 0;
    for (let i = n - 1; i >= n - k; i--)
        h = (h * power + (s.charCodeAt(i) - 96)) % modulo;
    if (h === hashValue) ans = n - k;
    for (let i = n - k - 1; i >= 0; i--) {
        h = (h - (s.charCodeAt(i + k) - 96) * pk % modulo + modulo) % modulo;
        h = (h * power + (s.charCodeAt(i) - 96)) % modulo;
        if (h === hashValue) ans = i;
    }
    return s.substring(ans, ans + k);
}
