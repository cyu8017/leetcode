// LeetCode 0880 - Decoded String at Index
// https://leetcode.com/problems/decoded-string-at-index/

export function decodeAtIndex(s: string, k: number): string {
    let size = 0;
    for (let i = 0; i < s.length; i++) {
        const ch = s[i];
        if (ch >= '0' && ch <= '9') size *= ch.charCodeAt(0) - 48;
        else size++;
    }
    let kk = k;
    for (let i = s.length - 1; i >= 0; i--) {
        const ch = s[i];
        kk %= size;
        if (kk === 0 && ch >= 'a' && ch <= 'z') return ch;
        if (ch >= '0' && ch <= '9') size = Math.floor(size / (ch.charCodeAt(0) - 48));
        else size--;
    }
    return "";
}
