// LeetCode 3744 - Find Kth Character in Expanded String
// https://leetcode.com/problems/find-kth-character-in-expanded-string/

export function kthCharacter(s: any, k: any): any {
    const words = s.trim().split(/\s+/);
    for (const w of words) {
        const m = (1 + w.length) * w.length / 2;
        if (k === m) return ' ';
        if (k > m) {
            k -= m + 1;
        } else {
            let cur = 0;
            for (let i = 0; ; i++) {
                cur += i + 1;
                if (k < cur) return w[i];
            }
        }
    }
    return ' ';
}
