// LeetCode 0917 - Reverse Only Letters
// https://leetcode.com/problems/reverse-only-letters/

/**
 * @param {string} s
 * @return {string}
 */
var reverseOnlyLetters = function(s) {
    const arr = s.split("");
    let i = 0, j = arr.length - 1;
    const isLetter = (c) => /[a-zA-Z]/.test(c);
    while (i < j) {
        while (i < j && !isLetter(arr[i])) i++;
        while (i < j && !isLetter(arr[j])) j--;
        const tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
        i++;
        j--;
    }
    return arr.join("");
};
