"use strict";
// LeetCode 1718 - Construct the Lexicographically Largest Valid Sequence
// https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/
function constructDistancedSequence(n) {
    const size = 2 * n - 1;
    const ans = new Array(size).fill(0);
    const used = new Array(n + 1).fill(false);
    const backtrack = (i) => {
        while (i < size && ans[i] !== 0) {
            i++;
        }
        if (i === size) {
            return true;
        }
        for (let value = n; value >= 1; value--) {
            if (used[value]) {
                continue;
            }
            if (value === 1) {
                ans[i] = 1;
                used[1] = true;
                if (backtrack(i + 1)) {
                    return true;
                }
                used[1] = false;
                ans[i] = 0;
            }
            else {
                const j = i + value;
                if (j < size && ans[j] === 0) {
                    ans[i] = value;
                    ans[j] = value;
                    used[value] = true;
                    if (backtrack(i + 1)) {
                        return true;
                    }
                    used[value] = false;
                    ans[i] = 0;
                    ans[j] = 0;
                }
            }
        }
        return false;
    };
    backtrack(0);
    return ans;
}
