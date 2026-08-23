// LeetCode 2832 - Maximal Range That Each Element Is Maximum in It
// https://leetcode.com/problems/maximal-range-that-each-element-is-maximum-in-it/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var maximumLength = function(nums) {
    const n = nums.length;
    const left = Array(n), right = Array(n);
    const st = [];
    for (let i = 0; i < n; i++) {
        while (st.length && nums[st[st.length - 1]] < nums[i]) st.pop();
        left[i] = st.length ? st[st.length - 1] : -1;
        st.push(i);
    }
    st.length = 0;
    for (let i = n - 1; i >= 0; i--) {
        while (st.length && nums[st[st.length - 1]] <= nums[i]) st.pop();
        right[i] = st.length ? st[st.length - 1] : n;
        st.push(i);
    }
    const ans = Array(n);
    for (let i = 0; i < n; i++) ans[i] = right[i] - left[i] - 1;
    return ans;
};
