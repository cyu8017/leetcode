// LeetCode 0859 - Buddy Strings
// https://leetcode.com/problems/buddy-strings/

class Solution {
    func buddyStrings(_ s: String, _ goal: String) -> Bool {
        if s.count != goal.count { return false }
        if s == goal {
            var seen = Set<Character>()
            for ch in s {
                if !seen.insert(ch).inserted { return true }
            }
            return false
        }
        let cs = Array(s), cg = Array(goal)
        var diffs = [(Character, Character)]()
        for i in 0..<cs.count where cs[i] != cg[i] {
            diffs.append((cs[i], cg[i]))
        }
        return diffs.count == 2 && diffs[0].0 == diffs[1].1 && diffs[0].1 == diffs[1].0
    }
}
