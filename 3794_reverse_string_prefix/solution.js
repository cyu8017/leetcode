// LeetCode 3794 - Reverse String Prefix
// https://leetcode.com/problems/reverse-string-prefix/

var reversePrefix = function(s, k) {
    const arr = s.split('');
    for (let i = 0, j = k - 1; i < j; i++, j--) {
        const t = arr[i]; arr[i] = arr[j]; arr[j] = t;
    }
    return arr.join('');
};
