// LeetCode 2281 - Sum of Total Strength of Wizards
// https://leetcode.com/problems/sum-of-total-strength-of-wizards/

var totalStrength = function(strength) {
    const mod = 1000000007;
    const n = strength.length;
    const left = new Array(n), right = new Array(n);
    const stack = [];
    for (let i = 0; i < n; i++) {
        while (stack.length && strength[stack[stack.length - 1]] >= strength[i]) stack.pop();
        left[i] = stack.length ? stack[stack.length - 1] : -1;
        stack.push(i);
    }
    stack.length = 0;
    for (let i = n - 1; i >= 0; i--) {
        while (stack.length && strength[stack[stack.length - 1]] > strength[i]) stack.pop();
        right[i] = stack.length ? stack[stack.length - 1] : n;
        stack.push(i);
    }
    const pref = new Array(n + 1).fill(0);
    const prefPref = new Array(n + 2).fill(0);
    for (let i = 0; i < n; i++) pref[i + 1] = (pref[i] + strength[i]) % mod;
    for (let i = 0; i <= n; i++) prefPref[i + 1] = (prefPref[i] + pref[i]) % mod;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const l = left[i] + 1, r = right[i] - 1;
        const leftSum = (prefPref[i + 1] - prefPref[l] + mod) % mod;
        const rightSum = (prefPref[r + 2] - prefPref[i + 1] + mod) % mod;
        const leftCnt = i - l + 1, rightCnt = r - i + 1;
        const contrib = (rightCnt * leftSum % mod - leftCnt * rightSum % mod + mod) % mod;
        ans = (ans + contrib * strength[i] % mod) % mod;
    }
    return ans;
};
