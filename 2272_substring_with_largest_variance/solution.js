// LeetCode 2272 - Substring With Largest Variance
// https://leetcode.com/problems/substring-with-largest-variance/

var largestVariance = function(s) {
    let ans = 0;
    for (let ai = 0; ai < 26; ai++) {
        for (let bi = 0; bi < 26; bi++) {
            if (ai === bi) continue;
            const a = String.fromCharCode(97 + ai), b = String.fromCharCode(97 + bi);
            let bal = 0, hasB = false;
            for (const c of s) {
                if (c === a) bal++;
                else if (c === b) { bal--; hasB = true; }
                if (hasB) ans = Math.max(ans, bal);
                if (bal < 0) { bal = 0; hasB = false; }
            }
        }
    }
    return ans;
};
