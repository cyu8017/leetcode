// LeetCode 1868 - Product of Two Run-Length Encoded Arrays
// https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/

/**
 * @param {number[][]} encoded1
 * @param {number[][]} encoded2
 * @return {number[][]}
 */
var findRLEArray = function(encoded1, encoded2) {
    const result = [];
    let i = 0, j = 0;
    let rem1 = encoded1[0][1], rem2 = encoded2[0][1];
    while (i < encoded1.length) {
        const take = Math.min(rem1, rem2);
        const value = encoded1[i][0] * encoded2[j][0];
        if (result.length && result[result.length - 1][0] === value) {
            result[result.length - 1][1] += take;
        } else {
            result.push([value, take]);
        }
        rem1 -= take;
        rem2 -= take;
        if (rem1 === 0) {
            i++;
            if (i < encoded1.length) rem1 = encoded1[i][1];
        }
        if (rem2 === 0) {
            j++;
            if (j < encoded2.length) rem2 = encoded2[j][1];
        }
    }
    return result;
};
