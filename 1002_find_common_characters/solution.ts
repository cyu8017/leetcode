// LeetCode 1002 - Find Common Characters
// https://leetcode.com/problems/find-common-characters/

function commonChars(words: string[]): string[] {
    const count = (w: string): number[] => {
        const freq = new Array(26).fill(0);
        for (const ch of w) freq[ch.charCodeAt(0) - 97]++;
        return freq;
    };
    let common = count(words[0]);
    for (let i = 1; i < words.length; i++) {
        const cur = count(words[i]);
        for (let j = 0; j < 26; j++) common[j] = Math.min(common[j], cur[j]);
    }
    const ans: string[] = [];
    for (let j = 0; j < 26; j++) {
        for (let k = 0; k < common[j]; k++) ans.push(String.fromCharCode(97 + j));
    }
    return ans;
}
