// LeetCode 3779 - Minimum Number Of Operations To Have Distinct Elements
// https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/

var minOperations = function(nums) {
    const st = new Set();
    for (let i = nums.length - 1; i >= 0; i--) {
        if (st.has(nums[i])) return Math.floor(i / 3) + 1;
        st.add(nums[i]);
    }
    return 0;
};
