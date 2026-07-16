// LeetCode 0139 - Word Break
// https://leetcode.com/problems/word-break/

export function wordBreak(s: string, wordDict: string[]): boolean {
    const words = new Set(wordDict);
    const possible = Array<boolean>(s.length + 1).fill(false);
    possible[0] = true;

    for (let end = 1; end <= s.length; end += 1) {
        for (let start = 0; start < end; start += 1) {
            if (possible[start] && words.has(s.slice(start, end))) {
                possible[end] = true;
                break;
            }
        }
    }

    return possible[s.length];
}