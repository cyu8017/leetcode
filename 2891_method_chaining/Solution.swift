// LeetCode 2891 - Method Chaining
// https://leetcode.com/problems/method-chaining/
// Pandas stand-in.

class Solution {
    func findHeavyAnimals(_ animals: [[Any]]) -> [[String: Any]] {
        func weight(_ r: [Any]) -> Int {
            return r[3] as? Int ?? 0
        }
        var filtered = animals.filter { weight($0) > 100 }
        filtered.sort { weight($0) > weight($1) }
        return filtered.map { ["name": $0[0]] }
    }
}
