// LeetCode 3216 - Lexicographically Smallest String After a Swap
// https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/

var getSmallestString = function(s) {
    const arr = s.split('');
    const n = arr.length;
    for (let i = 1; i < n; i++) {
        const a = arr[i - 1], b = arr[i];
        if (a > b && (a.charCodeAt(0) % 2) === (b.charCodeAt(0) % 2)) {
            arr[i - 1] = b; arr[i] = a;
            return arr.join('');
        }
    }
    return s;
};
