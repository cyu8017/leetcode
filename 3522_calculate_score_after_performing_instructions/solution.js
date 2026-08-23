// LeetCode 3522 - Calculate Score After Performing Instructions
// https://leetcode.com/problems/calculate-score-after-performing-instructions/

var calculateScore = function(instructions, values) {
    const n = values.length;
    const vis = new Array(n).fill(false);
    let ans = 0, i = 0;
    while (i >= 0 && i < n && !vis[i]) {
        vis[i] = true;
        if (instructions[i][0] === 'a') {
            ans += values[i];
            i += 1;
        } else {
            i += values[i];
        }
    }
    return ans;
};
