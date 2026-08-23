// LeetCode 3840 - House Robber V
// https://leetcode.com/problems/house-robber-v/

var rob = function(nums, colors) {
    const n = nums.length;
    let f = 0, g = nums[0];
    for (let i = 1; i < n; i++) {
        if (colors[i - 1] === colors[i]) {
            const nf = Math.max(f, g);
            g = f + nums[i];
            f = nf;
        } else {
            const nf = Math.max(f, g);
            g = nf + nums[i];
            f = nf;
        }
    }
    return Math.max(f, g);
};
