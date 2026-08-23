// LeetCode 3016 - Minimum Number of Pushes to Type Word II
// https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

var minimumPushes = function(word) {
    const cnt = new Array(26).fill(0);
    for (let i = 0; i < word.length; i++) cnt[word.charCodeAt(i) - 97]++;
    cnt.sort((a, b) => a - b);
    let ans = 0;
    for (let i = 0; i < 26; i++) ans += (((i / 8) | 0) + 1) * cnt[26 - i - 1];
    return ans;
};
