// LeetCode 1394 - Find Lucky Integer in an Array
// https://leetcode.com/problems/find-lucky-integer-in-an-array/

class Solution {
    func findLucky(_ arr: [Int]) -> Int {
        var c = [Int: Int]()
        for x in arr { c[x, default: 0] += 1 }
        return c.filter { $0.key == $0.value }.map { $0.key }.max() ?? -1
    }
}
