// LeetCode 3445 - Maximum Difference Between Even and Odd Frequency II
// https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/

var maxDifference = function(s, k) {
    const n = s.length;
    let ans = -1e9;
    for (let a = 0; a < 5; a++) {
        for (let b = 0; b < 5; b++) {
            if (a === b) continue;
            const prefA = new Array(n + 1).fill(0), prefB = new Array(n + 1).fill(0);
            for (let i = 0; i < n; i++) {
                prefA[i + 1] = prefA[i];
                prefB[i + 1] = prefB[i];
                if (s.charCodeAt(i) - 48 === a) prefA[i + 1]++;
                if (s.charCodeAt(i) - 48 === b) prefB[i + 1]++;
            }
            for (let i = 0; i < n; i++) {
                for (let j = i + k - 1; j < n; j++) {
                    const fa = prefA[j + 1] - prefA[i];
                    const fb = prefB[j + 1] - prefB[i];
                    if (fa % 2 === 1 && fb % 2 === 0 && fb > 0) {
                        if (fa - fb > ans) ans = fa - fb;
                    }
                }
            }
        }
    }
    return ans;
};
