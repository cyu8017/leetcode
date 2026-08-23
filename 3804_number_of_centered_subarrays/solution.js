// LeetCode 3804 - Number Of Centered Subarrays
// https://leetcode.com/problems/number-of-centered-subarrays/

var centeredSubarrays = function(nums) {
    const n = nums.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const st = new Set();
        let s = 0;
        for (let j = i; j < n; j++) {
            s += nums[j];
            st.add(nums[j]);
            if (st.has(s)) ans++;
        }
    }
    return ans;
};
