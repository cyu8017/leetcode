// LeetCode 2691 - Immutability Helper
// https://leetcode.com/problems/immutability-helper/

class Solution {
    func immutableHelper(_ obj: [String: Int], _ mutators: [([String: Int]) -> [String: Int]]) -> [[String: Int]] {
        mutators.map { $0(obj) }
    }
}
