// LeetCode 3676 - Count Bowl Subarrays
// https://leetcode.com/problems/count-bowl-subarrays/

export function bowlSubarrays(nums: any): any {
    const n = nums.length;
    let ans = 0;
    const ngr = new Array(n).fill(-1);
    const ngl = new Array(n).fill(-1);
    const stack = [];
    for (let i = n - 1; i >= 0; i--) {
        while (stack.length && nums[stack[stack.length - 1]] < nums[i]) stack.pop();
        if (stack.length) ngr[i] = stack[stack.length - 1];
        stack.push(i);
    }
    stack.length = 0;
    for (let i = 0; i < n; i++) {
        while (stack.length && nums[stack[stack.length - 1]] < nums[i]) stack.pop();
        if (stack.length) ngl[i] = stack[stack.length - 1];
        stack.push(i);
    }
    for (let i = 0; i < n; i++) {
        if (ngr[i] !== -1 && ngr[i] - i >= 2) ans++;
        if (ngl[i] !== -1 && i - ngl[i] >= 2) ans++;
    }
    return ans;
}
