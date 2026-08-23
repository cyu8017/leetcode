// LeetCode 0524 - Longest Word in Dictionary through Deleting
// https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

class Solution {
    findLongestWord(s, dictionary) {
        const isSubsequence = (word) => {
            let index = 0;
            for (const char of s) {
                if (index < word.length && word[index] === char) index += 1;
            }
            return index === word.length;
        };
        let best = "";
        for (const word of dictionary) {
            if (isSubsequence(word) && (word.length > best.length || (word.length === best.length && word < best))) {
                best = word;
            }
        }
        return best;
    }
}

module.exports = { Solution };
