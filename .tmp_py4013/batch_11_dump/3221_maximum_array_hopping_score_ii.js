// LeetCode 3221 - Maximum Array Hopping Score II
// https://leetcode.com/problems/maximum-array-hopping-score-ii/

var maxScore = function(nums) {
    const stk = [];
    for (let i = 0; i < nums.length; i++) {
        while (stk.length > 0 && nums[stk[stk.length - 1]] <= nums[i]) stk.pop();
        stk.push(i);
    }
    let ans = 0, cur = 0;
    for (const j of stk) {
        ans += (j - cur) * nums[j];
        cur = j;
    }
    return ans;
};
