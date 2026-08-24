// LeetCode 3597 - Partition String
// https://leetcode.com/problems/partition-string/

class Solution {
    func partitionString(_ s: String) -> [String] {
        var vis = Set<String>()
        var ans = [String]()
        var t = ""
        for c in s {
            t.append(c)
            if !vis.contains(t) {
                vis.insert(t)
                ans.append(t)
                t = ""
            }
        }
        return ans
    }
}
