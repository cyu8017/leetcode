// LeetCode 0425 - Word Squares
// https://leetcode.com/problems/word-squares/

export class Solution {
    wordSquares(words: string[]): string[][] {
        words.sort();
        const length = words[0].length;
        const prefixMap: Record<string, string[]> = { "": [...words] };
        for (const word of words) {
            for (let index = 0; index < word.length; index += 1) {
                const prefix = word.slice(0, index + 1);
                if (!prefixMap[prefix]) prefixMap[prefix] = [];
                prefixMap[prefix].push(word);
            }
        }

        const squares: string[][] = [];
        const current: string[] = [];

        const dfs = (row: number): void => {
            if (row === length) {
                squares.push([...current]);
                return;
            }
            const prefix = current.map((item) => item[row]).join("");
            for (const candidate of prefixMap[prefix] || []) {
                current.push(candidate);
                dfs(row + 1);
                current.pop();
            }
        };

        dfs(0);
        return squares;
    }
}
