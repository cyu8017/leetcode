// LeetCode 2942 - Find Words Containing Character
// https://leetcode.com/problems/find-words-containing-character/

export function findWordsContaining(words: any, x: any): any {
    const ans = [];
    for (let i = 0; i < words.length; i++) {
        if (words[i].indexOf(x) >= 0) ans.push(i);
    }
    return ans;
}
