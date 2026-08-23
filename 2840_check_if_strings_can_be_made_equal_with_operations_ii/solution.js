// LeetCode 2840 - Check if Strings Can be Made Equal With Operations II
// https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/

/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkStrings = function(s1, s2) {
    const even1 = Array(26).fill(0), odd1 = Array(26).fill(0);
    const even2 = Array(26).fill(0), odd2 = Array(26).fill(0);
    for (let i = 0; i < s1.length; i++) {
        if (i % 2 === 0) {
            even1[s1.charCodeAt(i) - 97]++;
            even2[s2.charCodeAt(i) - 97]++;
        } else {
            odd1[s1.charCodeAt(i) - 97]++;
            odd2[s2.charCodeAt(i) - 97]++;
        }
    }
    return even1.every((v, i) => v === even2[i]) && odd1.every((v, i) => v === odd2[i]);
};
