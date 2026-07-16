// LeetCode 0140 - Word Break II
// https://leetcode.com/problems/word-break-ii/

export function wordBreak(s: string, wordDict: string[]): string[] {
    const words = new Set(wordDict);
    const memo = new Map<number, string[]>();

    const dfs = (start: number): string[] => {
        const cached = memo.get(start);
        if (cached) return cached;
        if (start === s.length) return [""];

        const sentences: string[] = [];
        for (let end = start + 1; end <= s.length; end += 1) {
            const word = s.slice(start, end);
            if (!words.has(word)) continue;

            for (const tail of dfs(end)) {
                sentences.push(tail ? `${word} ${tail}` : word);
            }
        }
        memo.set(start, sentences);
        return sentences;
    };

    return dfs(0);
}