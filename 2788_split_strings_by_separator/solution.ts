// LeetCode 2788 - Split Strings by Separator
// https://leetcode.com/problems/split-strings-by-separator/

export function splitWordsBySeparator(words: string[], separator: string): string[] {
    const ans = [];
    for (const w of words) {
        let start = 0;
        for (let i = 0; i <= w.length; i++) {
            if (i === w.length || w[i] === separator) {
                if (i > start) ans.push(w.slice(start, i));
                start = i + 1;
            }
        }
    }
    return ans;
}
