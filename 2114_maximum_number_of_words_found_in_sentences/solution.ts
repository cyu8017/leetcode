// LeetCode 2114 - Maximum Number of Words Found in Sentences
// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

export function mostWordsFound(sentences: string[]): number {
    let ans = 0;
    for (const s of sentences) {
        let c = 1;
        for (let i = 0; i < s.length; i++) if (s[i] === ' ') c++;
        ans = Math.max(ans, c);
    }
    return ans;
}
