// LeetCode 3978 - Unique Middle Element
// https://leetcode.com/problems/unique-middle-element/
var isMiddleElementUnique = function(nums) {
        let mid = nums[nums.length / 2];
        let cnt = 0;
        for (const x of nums) {
            if (x == mid) cnt++;
        }
        return cnt == 1;
    
};
