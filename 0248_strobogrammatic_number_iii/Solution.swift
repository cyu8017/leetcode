// LeetCode 0248 - Strobogrammatic Number III
// https://leetcode.com/problems/strobogrammatic-number-iii/

class Solution {
    private let pairs: [(String, String)] = [
        ("0", "0"),
        ("1", "1"),
        ("6", "9"),
        ("8", "8"),
        ("9", "6"),
    ]

    func strobogrammaticInRange(_ low: String, _ high: String) -> Int {
        let lowValue = Int(low) ?? 0
        let highValue = Int(high) ?? 0
        var count = 0

        for length in low.count...high.count {
            for value in build(0, length - 1) {
                let numeric = Int(value) ?? 0
                if lowValue <= numeric && numeric <= highValue {
                    count += 1
                }
            }
        }
        return count
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
