// LeetCode 2957 - Remove Adjacent Almost-Equal Characters
// https://leetcode.com/problems/remove-adjacent-almost-equal-characters/

var removeAlmostEqualCharacters = function(word) {
    let ans = 0, i = 1;
    const n = word.length;
    while (i < n) {
        if (Math.abs(word.charCodeAt(i) - word.charCodeAt(i - 1)) <= 1) {
            ans++;
            i += 2;
        } else i++;
    }
    return ans;
};
