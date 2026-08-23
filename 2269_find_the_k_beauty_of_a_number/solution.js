// LeetCode 2269 - Find the K-Beauty of a Number
// https://leetcode.com/problems/find-the-k-beauty-of-a-number/

var divisorSubstrings = function(num, k) {
    const s = String(num);
    let ans = 0;
    for (let i = 0; i + k <= s.length; i++) {
        let sub = 0;
        for (let j = 0; j < k; j++) sub = sub * 10 + (s.charCodeAt(i + j) - 48);
        if (sub !== 0 && num % sub === 0) ans++;
    }
    return ans;
};
