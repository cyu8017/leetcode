// LeetCode 3542 - Minimum Operations to Convert All Elements to Zero
// https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

var minOperations = function(nums) {
    const stk = [];
    let ans = 0;
    for (const x of nums) {
        while (stk.length > 0 && stk[stk.length - 1] > x) {
            ans++;
            stk.pop();
        }
        if (x !== 0 && (stk.length === 0 || stk[stk.length - 1] !== x)) stk.push(x);
    }
    ans += stk.length;
    return ans;
};
