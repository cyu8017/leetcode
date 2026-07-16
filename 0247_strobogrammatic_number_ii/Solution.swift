// LeetCode 0247 - Strobogrammatic Number II
// https://leetcode.com/problems/strobogrammatic-number-ii/

class Solution {
    private let pairs: [(String, String)] = [
        ("0", "0"),
        ("1", "1"),
        ("6", "9"),
        ("8", "8"),
        ("9", "6"),
    ]

    func findStrobogrammatic(_ n: Int) -> [String] {
        return build(0, n - 1)
    }

    private func build(_ left: Int, _ right: Int) -> [String] {
        if left > right {
            return [""]
        }
        if left == right {
            return ["0", "1", "8"]
        }
        var result: [String] = []
        for (start, end) in pairs {
            if left == 0 && start == "0" {
                continue
            }
            for middle in build(left + 1, right - 1) {
                result.append(start + middle + end)
            }
        }
        return result
    }
}
