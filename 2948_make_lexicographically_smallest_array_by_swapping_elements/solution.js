// LeetCode 2948 - Make Lexicographically Smallest Array by Swapping Elements
// https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

var lexicographicallySmallestArray = function(nums, limit) {
    const n = nums.length;
    const idx = Array.from({length: n}, (_, i) => i);
    idx.sort((a, b) => nums[a] - nums[b]);
    const ans = new Array(n);
    for (let i = 0; i < n; ) {
        let j = i + 1;
        while (j < n && nums[idx[j]] - nums[idx[j - 1]] <= limit) j++;
        const groupIdx = [];
        for (let t = 0; t < j - i; t++) groupIdx.push(idx[i + t]);
        groupIdx.sort((a, b) => a - b);
        for (let t = 0; t < j - i; t++) ans[groupIdx[t]] = nums[idx[i + t]];
        i = j;
    }
    return ans;
};
