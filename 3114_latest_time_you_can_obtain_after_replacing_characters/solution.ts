// LeetCode 3114 - Latest Time You Can Obtain After Replacing Characters
// https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/

export function findLatestTime(s: string): string {
    for (let h = 11; ; h--) {
        for (let m = 59; m >= 0; m--) {
            const t = String(h).padStart(2, '0') + ':' + String(m).padStart(2, '0');
            let ok = true;
            for (let i = 0; i < 5; i++) {
                if (s[i] !== '?' && s[i] !== t[i]) { ok = false; break; }
            }
            if (ok) return t;
        }
    }
}
