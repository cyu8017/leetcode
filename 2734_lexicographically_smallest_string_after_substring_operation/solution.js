// LeetCode 2734 - Lexicographically Smallest String After Substring Operation
// https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/

/**
 * @param {string} s
 * @return {string}
 */
var smallestString = function(s) {
    const arr = s.split('');
    const n = arr.length;
    let i = 0;
    while (i < n && arr[i] === 'a') i++;
    if (i === n) {
        arr[n - 1] = 'z';
        return arr.join('');
    }
    while (i < n && arr[i] !== 'a') {
        arr[i] = String.fromCharCode(arr[i].charCodeAt(0) - 1);
        i++;
    }
    return arr.join('');
};
