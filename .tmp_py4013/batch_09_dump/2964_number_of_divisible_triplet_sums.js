// LeetCode 2964 - Number of Divisible Triplet Sums
// https://leetcode.com/problems/number-of-divisible-triplet-sums/

var divisibleTripletCount = function(nums, d) {
    const n = nums.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const freq = new Map();
        for (let j = i + 1; j < n; j++) {
            const need = (d - (nums[i] + nums[j]) % d) % d;
            ans += freq.get(need) || 0;
            const key = nums[j] % d;
            freq.set(key, (freq.get(key) || 0) + 1);
        }
    }
    return ans;
};
