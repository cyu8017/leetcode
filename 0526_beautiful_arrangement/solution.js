// LeetCode 0526 - Beautiful Arrangement
// https://leetcode.com/problems/beautiful-arrangement/

class Solution {
    countArrangement(n) {
        let count = 0;
        const backtrack = (index, used) => {
            if (index === n + 1) {
                count += 1;
                return;
            }
            for (let num = 1; num <= n; num += 1) {
                if (used.has(num)) continue;
                if (index % num === 0 || num % index === 0) {
                    used.add(num);
                    backtrack(index + 1, used);
                    used.delete(num);
                }
            }
        };
        backtrack(1, new Set());
        return count;
    }
}

module.exports = { Solution };
