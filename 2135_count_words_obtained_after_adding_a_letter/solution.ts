// LeetCode 2135 - Count Words Obtained After Adding a Letter
// https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

export function wordCount(startWords: string[], targetWords: string[]): number {
    const mask = (w) => {
        let m = 0;
        for (let i = 0; i < w.length; i++) m |= 1 << (w.charCodeAt(i) - 97);
        return m;
    };
    const have = new Set();
    for (const w of startWords) have.add(mask(w));
    let ans = 0;
    for (const w of targetWords) {
        const m = mask(w);
        for (let i = 0; i < w.length; i++) {
            if (have.has(m ^ (1 << (w.charCodeAt(i) - 97)))) { ans++; break; }
        }
    }
    return ans;
}
