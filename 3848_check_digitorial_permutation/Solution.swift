// LeetCode 3848 - Check Digitorial Permutation
// https://leetcode.com/problems/check-digitorial-permutation/

class Solution {
    func isDigitorialPermutation(_ n: Int) -> Bool {
        var f = [Int](repeating: 0, count: 10)
        f[0] = 1
        for i in 1..<10 { f[i] = f[i - 1] * i }
        var x = 0, y = n
        while y > 0 {
            x += f[y % 10]
            y /= 10
        }
        return String(String(x).sorted()) == String(String(n).sorted())
    }
}
