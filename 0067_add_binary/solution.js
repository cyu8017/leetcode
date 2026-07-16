// LeetCode 0067 - Add Binary
// https://leetcode.com/problems/add-binary/

/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    let i = a.length - 1;
    let j = b.length - 1;
    let carry = 0;
    const result = [];

    while (i >= 0 || j >= 0 || carry) {
        let total = carry;
        if (i >= 0) {
            total += Number(a[i]);
            i -= 1;
        }
        if (j >= 0) {
            total += Number(b[j]);
            j -= 1;
        }
        result.push(String(total % 2));
        carry = Math.floor(total / 2);
    }

    return result.reverse().join("");
};
