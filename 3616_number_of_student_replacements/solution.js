// LeetCode 3616 - Number of Student Replacements
// https://leetcode.com/problems/number-of-student-replacements/

var totalReplacements = function(ranks) {
    let ans = 0, cur = ranks[0];
    for (const x of ranks) {
        if (x < cur) {
            cur = x;
            ans++;
        }
    }
    return ans;
};
