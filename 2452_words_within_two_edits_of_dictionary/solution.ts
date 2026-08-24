// LeetCode 2452 - Words Within Two Edits of Dictionary
// https://leetcode.com/problems/words-within-two-edits-of-dictionary/

export function twoEditWords(queries: string[], dictionary: string[]): string[] {
    const ans = [];
    for (const q of queries) {
        let ok = false;
        for (const d of dictionary) {
            let diff = 0;
            for (let i = 0; i < q.length; i++) {
                if (q[i] !== d[i]) {
                    if (++diff > 2) break;
                }
            }
            if (diff <= 2) { ok = true; break; }
        }
        if (ok) ans.push(q);
    }
    return ans;
}
