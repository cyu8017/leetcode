// LeetCode 0030 - Substring with Concatenation of All Words
// https://leetcode.com/problems/substring-with-concatenation-of-all-words/

export function findSubstring(s: string, words: string[]): number[] {
    if (!words.length || !s.length) {
        return [];
    }

    const wordLen = words[0].length;
    const wordCount = words.length;
    const need = new Map<string, number>();
    for (const word of words) {
        need.set(word, (need.get(word) || 0) + 1);
    }

    const result: number[] = [];

    for (let start = 0; start < wordLen; start++) {
        let left = start;
        const counts = new Map<string, number>();
        let used = 0;

        for (let right = start; right <= s.length - wordLen; right += wordLen) {
            const word = s.slice(right, right + wordLen);
            if (!need.has(word)) {
                counts.clear();
                used = 0;
                left = right + wordLen;
                continue;
            }

            counts.set(word, (counts.get(word) || 0) + 1);
            used++;
            while ((counts.get(word) || 0) > need.get(word)!) {
                const leftWord = s.slice(left, left + wordLen);
                counts.set(leftWord, (counts.get(leftWord) || 0) - 1);
                used--;
                left += wordLen;
            }

            if (used === wordCount) {
                result.push(left);
            }
        }
    }

    return result.sort((a, b) => a - b);
}
