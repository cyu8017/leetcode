// LeetCode 1073 - Adding Two Negabinary Numbers
// https://leetcode.com/problems/adding-two-negabinary-numbers/

/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number[]}
 */
var addNegabinary = function(arr1, arr2) {
    let i = arr1.length - 1;
    let j = arr2.length - 1;
    let carry = 0;
    const ans = [];
    while (i >= 0 || j >= 0 || carry) {
        let total = carry;
        if (i >= 0) total += arr1[i--];
        if (j >= 0) total += arr2[j--];
        ans.push(total & 1);
        carry = -(total >> 1);
    }
    while (ans.length > 1 && ans[ans.length - 1] === 0) ans.pop();
    return ans.reverse();
};
