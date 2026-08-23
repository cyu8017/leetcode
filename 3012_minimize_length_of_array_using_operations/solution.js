// LeetCode 3012 - Minimize Length of Array Using Operations
// https://leetcode.com/problems/minimize-length-of-array-using-operations/

var minimumArrayLength = function(nums) {
    let mi = nums[0];
    for (const x of nums) if (x < mi) mi = x;
    let cnt = 0;
    for (const x of nums) {
        if (x % mi !== 0) return 1;
        if (x === mi) cnt++;
    }
    return ((cnt + 1) / 2) | 0;
};
