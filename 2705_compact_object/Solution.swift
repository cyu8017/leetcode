// LeetCode 2705 - Compact Object
// https://leetcode.com/problems/compact-object/

class Solution {
    func compactObject(_ obj: [Int]) -> [Int] {
        obj.filter { $0 != 0 }
    }
}
