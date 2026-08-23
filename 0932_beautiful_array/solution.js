// LeetCode 0932 - Beautiful Array
// https://leetcode.com/problems/beautiful-array/

/**
 * @param {number} n
 * @return {number[]}
 */
var beautifulArray = function(n) {
    let res = [1];
    while (res.length < n) {
        const tmp = [];
        for (const x of res) if (x * 2 - 1 <= n) tmp.push(x * 2 - 1);
        for (const x of res) if (x * 2 <= n) tmp.push(x * 2);
        res = tmp;
    }
    return res;
};
