// LeetCode 3640 - Trionic Array II
// https://leetcode.com/problems/trionic-array-ii/

var maxSumTrionic = function(nums) {
    const n = nums.length;
    let i = 0;
    let ans = -Infinity;
    while (i < n) {
        const l = i;
        for (i++; i < n && nums[i - 1] < nums[i];) i++;
        if (i === l + 1) continue;
        const p = i - 1;
        let s = nums[p - 1] + nums[p];
        while (i < n && nums[i - 1] > nums[i]) {
            s += nums[i];
            i++;
        }
        if (i === p + 1 || i === n || nums[i - 1] === nums[i]) continue;
        const q = i - 1;
        s += nums[i];
        i++;
        let mx = 0, t = 0;
        while (i < n && nums[i - 1] < nums[i]) {
            t += nums[i];
            i++;
            mx = Math.max(mx, t);
        }
        s += mx;
        mx = t = 0;
        for (let j = p - 2; j >= l; j--) {
            t += nums[j];
            mx = Math.max(mx, t);
        }
        s += mx;
        ans = Math.max(ans, s);
        i = q;
    }
    return ans;
};
