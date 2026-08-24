// LeetCode 2677 - Chunk Array
// https://leetcode.com/problems/chunk-array/

class Solution {
    func chunk(_ arr: [Int], _ size: Int) -> [[Int]] {
        var ans: [[Int]] = []
        var i = 0
        while i < arr.count {
            let end = min(arr.count, i + size)
            ans.append(Array(arr[i..<end]))
            i += size
        }
        return ans
    }
}
