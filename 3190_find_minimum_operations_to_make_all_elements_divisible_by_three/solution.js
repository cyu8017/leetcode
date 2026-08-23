// LeetCode 3190 - Find Minimum Operations to Make All Elements Divisible by Three
// https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

var minimumOperations = function(nums) {
    let ans = 0;
    for (const x of nums) if (x % 3 !== 0) ans++;
    return ans;
};
