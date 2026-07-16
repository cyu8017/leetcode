// LeetCode 0191 - Number of 1 Bits
class Solution {
    func hammingWeight(_ n: Int) -> Int {
        var value = n
        var count = 0
        while value != 0 {
            value &= value - 1
            count += 1
        }
        return count
    }
}