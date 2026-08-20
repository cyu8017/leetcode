// LeetCode 1317 - Convert Integer to the Sum of Two No-Zero Integers
// https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

class Solution {
    func getNoZeroIntegers(_ n: Int) -> [Int] {
        func noZero(_ x: Int) -> Bool {
            var x = x
            while x > 0 {
                if x % 10 == 0 { return false }
                x /= 10
            }
            return true
        }
        for a in 1..<n where noZero(a) && noZero(n - a) { return [a, n - a] }
        return []
    }
}
