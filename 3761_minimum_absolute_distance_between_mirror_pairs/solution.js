// LeetCode 3761 - Minimum Absolute Distance Between Mirror Pairs
// https://leetcode.com/problems/minimum_absolute_distance_between_mirror_pairs/

var minMirrorPairDistance = function(nums) {
    const reverse = (x) => {
        let y = 0;
        for (; x > 0; x = Math.floor(x / 10)) y = y * 10 + x % 10;
        return y;
    };
    const n = nums.length;
    const pos = new Map();
    let ans = n + 1;
    for (let i = 0; i < n; i++) {
        if (pos.has(nums[i])) ans = Math.min(ans, i - pos.get(nums[i]));
        pos.set(reverse(nums[i]), i);
    }
    return ans > n ? -1 : ans;
};
