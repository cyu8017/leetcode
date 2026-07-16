// LeetCode 0089 - Gray Code
// https://leetcode.com/problems/gray-code/

class Solution {
    func grayCode(_ n: Int) -> [Int] {
        let size = 1 << n
        var result = [Int]()
        result.reserveCapacity(size)
        for i in 0..<size {
            result.append(i ^ (i >> 1))
        }
        return result
    }
}
