// LeetCode 3167 - Better Compression of String
// https://leetcode.com/problems/better-compression-of-string/

export function betterCompression(compressed: string): string {
    const cnt = new Array(26).fill(0);
    const n = compressed.length;
    for (let i = 0; i < n; ) {
        const c = compressed[i];
        let j = i + 1, x = 0;
        while (j < n) {
            const d = compressed[j];
            if (d < '0' || d > '9') break;
            x = x * 10 + (d.charCodeAt(0) - 48);
            j++;
        }
        cnt[c.charCodeAt(0) - 97] += x;
        i = j;
    }
    let ans = '';
    for (let c = 0; c < 26; c++) {
        if (cnt[c] > 0) ans += String.fromCharCode(97 + c) + String(cnt[c]);
    }
    return ans;
}
