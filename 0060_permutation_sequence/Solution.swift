// LeetCode 0060 - Permutation Sequence
// https://leetcode.com/problems/permutation-sequence/

class Solution {
    func getPermutation(_ n: Int, _ k: Int) -> String {
        var numbers = Array(1...n)
        var factorials = Array(repeating: 1, count: n)

        for i in 1..<n {
            factorials[i] = factorials[i - 1] * i
        }

        var remaining = k - 1
        var result = ""

        for i in stride(from: n - 1, through: 0, by: -1) {
            let index = remaining / factorials[i]
            result.append(String(numbers[index]))
            numbers.remove(at: index)
            remaining %= factorials[i]
        }

        return result
    }
}
