// LeetCode 0244 - Shortest Word Distance II
// https://leetcode.com/problems/shortest-word-distance-ii/

class WordDistance {
    /**
     * @param {string[]} wordsDict
     */
    constructor(wordsDict) {
        this.positions = new Map();
        for (let index = 0; index < wordsDict.length; index++) {
            const word = wordsDict[index];
            if (!this.positions.has(word)) {
                this.positions.set(word, []);
            }
            this.positions.get(word).push(index);
        }
    }

    /**
     * @param {string} word1
     * @param {string} word2
     * @return {number}
     */
    shortest(word1, word2) {
        const left = this.positions.get(word1);
        const right = this.positions.get(word2);
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

module.exports = { WordDistance };
