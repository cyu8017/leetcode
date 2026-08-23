// LeetCode 3541 - Find Most Frequent Vowel and Consonant
// https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

var maxFreqSum = function(s) {
    const cnt = new Array(26).fill(0);
    for (const c of s) cnt[c.charCodeAt(0) - 97]++;
    let a = 0, b = 0;
    for (let i = 0; i < 26; i++) {
        const c = String.fromCharCode(97 + i);
        if ('aeiou'.includes(c)) a = Math.max(a, cnt[i]);
        else b = Math.max(b, cnt[i]);
    }
    return a + b;
};
