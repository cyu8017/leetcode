// LeetCode 0819 - Most Common Word
// https://leetcode.com/problems/most-common-word/

export function mostCommonWord(paragraph: string, banned: string[]): string {
    const bannedSet = new Set(banned);
    const counts = new Map();
    let word = "";
    let best = "", bestCount = 0;
    for (let i = 0; i <= paragraph.length; i++) {
        const ch = i < paragraph.length ? paragraph[i] : ' ';
        if (/[a-zA-Z]/.test(ch)) {
            word += ch.toLowerCase();
        } else if (word.length > 0) {
            const w = word;
            word = "";
            if (!bannedSet.has(w)) {
                const c = (counts.get(w) || 0) + 1;
                counts.set(w, c);
                if (c > bestCount) {
                    bestCount = c;
                    best = w;
                }
            }
        }
    }
    return best;
}
