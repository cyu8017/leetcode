// LeetCode 3285 - Find Indices of Stable Mountains
// https://leetcode.com/problems/find-indices-of-stable-mountains/

var stableMountains = function(height, threshold) {
    const ans = [];
    for (let i = 1; i < height.length; i++) {
        if (height[i - 1] > threshold) ans.push(i);
    }
    return ans;
};
