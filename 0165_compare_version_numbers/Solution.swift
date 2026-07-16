// LeetCode 0165 - Compare Version Numbers
// https://leetcode.com/problems/compare-version-numbers/

class Solution {
    func compareVersion(_ version1: String, _ version2: String) -> Int {
        let first = version1.split(separator: ".").map { Int($0)! }
        let second = version2.split(separator: ".").map { Int($0)! }
        for index in 0..<max(first.count, second.count) {
            let a = index < first.count ? first[index] : 0
            let b = index < second.count ? second[index] : 0
            if a != b { return a < b ? -1 : 1 }
        }
        return 0
    }
}