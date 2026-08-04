// LeetCode 1389: Create Target Array In The Given Order

var createTargetArray = function(nums, index) {
    const target = [];
    for (let i = 0; i < nums.length; i++) target.splice(index[i], 0, nums[i]);
    return target;
};
