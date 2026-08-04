// LeetCode 1400: Construct K Palindrome Strings

var canConstruct = function(s, k) {
    if (s.length < k) return false;
    const count = Array(26).fill(0);
    for (const ch of s) count[ch.charCodeAt(0) - 97]++;
    return count.filter(value => value % 2).length <= k;
};
