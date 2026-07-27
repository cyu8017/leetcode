// LeetCode 1640 - Check Array Formation Through Concatenation
// https://leetcode.com/problems/check-array-formation-through-concatenation/

class Solution {
    func canFormArray(_ arr: [Int], _ pieces: [[Int]]) -> Bool {
        var byFirst = [Int: [Int]]()
        for p in pieces { byFirst[p[0]] = p }
        var i = 0
        while i < arr.count {
            guard let p = byFirst[arr[i]] else { return false }
            if Array(arr[i..<(i + p.count)]) != p { return false }
            i += p.count
        }
        return true
    }
}
