// LeetCode 0267 - Palindrome Permutation II
// https://leetcode.com/problems/palindrome-permutation-ii/

class Solution {
    func generatePalindromes(_ s: String) -> [String] {
        var counts: [Character: Int] = [:]
        for char in s {
            counts[char, default: 0] += 1
        }

        let oddChars = counts.filter { $0.value % 2 != 0 }.map(\.key)
        if oddChars.count > 1 {
            return []
        }
        let middle = oddChars.count == 1 ? String(oddChars[0]) : ""

        var half: [Character] = []
        for char in counts.keys.sorted() {
            let count = counts[char]! / 2
            half.append(contentsOf: Array(repeating: char, count: count))
        }

        var result: [String] = []
        var used = Array(repeating: false, count: half.count)
        var path: [Character] = []

        func backtrack() {
            if path.count == half.count {
                let prefix = String(path)
                result.append(prefix + middle + String(prefix.reversed()))
                return
            }
            for index in half.indices {
                if used[index] {
                    continue
                }
                if index > 0 && half[index] == half[index - 1] && !used[index - 1] {
                    continue
                }
                used[index] = true
                path.append(half[index])
                backtrack()
                path.removeLast()
                used[index] = false
            }
        }

        backtrack()
        return result
    }
}
