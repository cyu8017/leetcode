// LeetCode 3557 - Find Maximum Number of Non Intersecting Substrings
// https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/

var maxSubstrings = function(word) {
    let ans = 0;
    const first = new Map();
    for (let i = 0; i < word.length; i++) {
        const c = word[i];
        if (!first.has(c)) first.set(c, i);
        else if (i - first.get(c) + 1 >= 4) {
            ans++;
            first.clear();
        }
    }
    return ans;
};
