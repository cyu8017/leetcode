// LeetCode 0728 - Self Dividing Numbers
// https://leetcode.com/problems/self-dividing-numbers/

class Solution {
    func selfDividingNumbers(_ left: Int, _ right: Int) -> [Int] {
        func ok(_ n: Int) -> Bool {
            var x = n
            while x > 0 {
                let d = x % 10
                if d == 0 || n % d != 0 { return false }
                x /= 10
            }
            return true
        }
        return (left...right).filter(ok)
    }
}
