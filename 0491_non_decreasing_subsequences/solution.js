// LeetCode 0491 - Non-decreasing Subsequences
// https://leetcode.com/problems/non-decreasing-subsequences/

class Solution {
    findSubsequences(nums) {
        const result = new Set();

        const backtrack = (start, path) => {
            if (path.length >= 2) result.add(path.join(","));
            const used = new Set();
            for (let index = start; index < nums.length; index += 1) {
                if (used.has(nums[index])) continue;
                if (path.length && nums[index] < path[path.length - 1]) continue;
                used.add(nums[index]);
                path.push(nums[index]);
                backtrack(index + 1, path);
                path.pop();
            }
        };

        backtrack(0, []);
        return [...result].sort().map((entry) => entry.split(",").map(Number));
    }
}

module.exports = { Solution };
