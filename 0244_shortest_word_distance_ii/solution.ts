// LeetCode 0244 - Shortest Word Distance II
// https://leetcode.com/problems/shortest-word-distance-ii/

export class WordDistance {
    private readonly positions = new Map<string, number[]>();

    constructor(wordsDict: string[]) {
        for (let index = 0; index < wordsDict.length; index++) {
            const word = wordsDict[index];
            const list = this.positions.get(word) ?? [];
            list.push(index);
            this.positions.set(word, list);
        }
    }

    shortest(word1: string, word2: string): number {
        const left = this.positions.get(word1)!;
        const right = this.positions.get(word2)!;
        let i = 0;
        let j = 0;
        let best = Number.POSITIVE_INFINITY;
        while (i < left.length && j < right.length) {
            best = Math.min(best, Math.abs(left[i] - right[j]));
            if (left[i] <= right[j]) {
                i++;
            } else {
                j++;
            }
        }
        return best;
    }
}
