// LeetCode 3478 - Choose K Elements With Maximum Sum
// https://leetcode.com/problems/choose-k-elements-with-maximum-sum/

var findMaxSum = function(nums1, nums2, k) {
    const n = nums1.length;
    const arr = [];
    for (let i = 0; i < n; i++) arr.push([nums1[i], nums2[i], i]);
    arr.sort((a, b) => a[0] - b[0]);
    const ans = new Array(n);
    const h = [];
    let sum = 0;
    const push = (v) => { h.push(v); h.sort((a, b) => a - b); };
    const poll = () => h.shift();
    for (let i = 0; i < n; ) {
        const v = arr[i][0];
        const start = i;
        while (i < n && arr[i][0] === v) i++;
        for (let t = start; t < i; t++) ans[arr[t][2]] = sum;
        for (let t = start; t < i; t++) {
            push(arr[t][1]);
            sum += arr[t][1];
            if (h.length > k) sum -= poll();
        }
    }
    return ans;
};
