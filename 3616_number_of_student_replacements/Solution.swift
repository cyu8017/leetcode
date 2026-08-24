// LeetCode 3616 - Number of Student Replacements
// https://leetcode.com/problems/number-of-student-replacements/

class Solution {
    func totalReplacements(_ ranks: [Int]) -> Int {
        var ans = 0, cur = ranks[0]
        for x in ranks {
            if x < cur { cur = x; ans += 1 }
        }
        return ans
    }
}
