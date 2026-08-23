// LeetCode 3835 - Count Subarrays With Cost Less Than Or Equal To K
// https://leetcode.com/problems/count_subarrays_with_cost_less_than_or_equal_to_k/

var countSubarrays = function(nums, k) {
    let ans = 0;
    const q1 = [], q2 = [];
    let l = 0;
    for (let r = 0; r < nums.length; r++) {
        const x = nums[r];
        while (q1.length && nums[q1[q1.length - 1]] <= x) q1.pop();
        while (q2.length && nums[q2[q2.length - 1]] >= x) q2.pop();
        q1.push(r);
        q2.push(r);
        while (l < r && (nums[q1[0]] - nums[q2[0]]) * (r - l + 1) > k) {
            l++;
            if (q1[0] < l) q1.shift();
            if (q2[0] < l) q2.shift();
        }
        ans += r - l + 1;
    }
    return ans;
};
