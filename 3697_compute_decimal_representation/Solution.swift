// LeetCode 3697 - Compute Decimal Representation
// https://leetcode.com/problems/compute-decimal-representation/

class Solution {
    func decimalRepresentation(_ n: Int) -> [Int] {
        var n = n
        var ans = [Int]()
        var p = 1
        while n > 0 {
            let v = n % 10
            n /= 10
            if v != 0 { ans.append(p * v) }
            p *= 10
        }
        return ans.reversed()
    }
}
