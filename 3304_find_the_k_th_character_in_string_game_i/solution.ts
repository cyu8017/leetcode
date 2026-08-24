// LeetCode 3304 - Find the K-th Character in String Game I
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

export function kthCharacter(k: any): any {
    let s = 'a';
    while (s.length < k) {
        const n = s.length;
        let add = '';
        for (let i = 0; i < n; i++) {
            add += String.fromCharCode(97 + ((s.charCodeAt(i) - 97 + 1) % 26));
        }
        s += add;
    }
    return s[k - 1];
}
