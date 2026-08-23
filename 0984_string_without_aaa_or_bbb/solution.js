// LeetCode 0984 - String Without AAA or BBB
// https://leetcode.com/problems/string-without-aaa-or-bbb/

/**
 * @param {number} a
 * @param {number} b
 * @return {string}
 */
var strWithout3a3b = function(a, b) {
    let ans = "";
    while (a > 0 || b > 0) {
        let writeA;
        const len = ans.length;
        if (len >= 2 && ans[len - 1] === ans[len - 2])
            writeA = ans[len - 1] === 'b';
        else
            writeA = a >= b;
        if (writeA) { ans += 'a'; a--; }
        else { ans += 'b'; b--; }
    }
    return ans;
};
