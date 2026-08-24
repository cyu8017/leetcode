// LeetCode 2416 - Sum of Prefix Scores of Strings
// https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

export function sumPrefixScores(words: string[]): number[] {
    const root = { child: Array(26).fill(null), cnt: 0 };
    for (const w of words) {
        let cur = root;
        for (let i = 0; i < w.length; i++) {
            const c = w.charCodeAt(i) - 97;
            if (!cur.child[c]) cur.child[c] = { child: Array(26).fill(null), cnt: 0 };
            cur = cur.child[c];
            cur.cnt++;
        }
    }
    const ans = Array(words.length);
    for (let i = 0; i < words.length; i++) {
        let cur = root, sum = 0;
        const w = words[i];
        for (let j = 0; j < w.length; j++) {
            cur = cur.child[w.charCodeAt(j) - 97];
            sum += cur.cnt;
        }
        ans[i] = sum;
    }
    return ans;
}
