// LeetCode 0087 - Scramble String
// https://leetcode.com/problems/scramble-string/

class Solution {
    private var memo = [String: Bool]()

    func isScramble(_ s1: String, _ s2: String) -> Bool {
        let key = s1 + "#" + s2
        if let cached = memo[key] {
            return cached
        }
        if s1 == s2 {
            memo[key] = true
            return true
        }
        if s1.sorted() != s2.sorted() {
            memo[key] = false
            return false
        }

        let n = s1.count
        let a = Array(s1)
        let b = Array(s2)
        for i in 1..<n {
            let aLeft = String(a[0..<i])
            let aRight = String(a[i..<n])
            let bLeft = String(b[0..<i])
            let bRight = String(b[i..<n])
            let bSwapLeft = String(b[(n - i)..<n])
            let bSwapRight = String(b[0..<(n - i)])

            if isScramble(aLeft, bLeft) && isScramble(aRight, bRight) {
                memo[key] = true
                return true
            }
            if isScramble(aLeft, bSwapLeft) && isScramble(aRight, bSwapRight) {
                memo[key] = true
                return true
            }
        }
        memo[key] = false
        return false
    }
}
