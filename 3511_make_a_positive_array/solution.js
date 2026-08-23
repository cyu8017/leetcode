// LeetCode 3511 - Make a Positive Array
// https://leetcode.com/problems/make-a-positive-array/

var makeArrayPositive = function(nums) {
    let ans = 0, l = -1;
    let preMx = 0, s = 0;
    for (let r = 0; r < nums.length; r++) {
        s += nums[r];
        if (r - l > 2 && s <= preMx) {
            ans++;
            l = r;
            preMx = 0;
            s = 0;
        } else if (r - l >= 2) {
            preMx = Math.max(preMx, s - nums[r] - nums[r - 1]);
        }
    }
    return ans;
};
