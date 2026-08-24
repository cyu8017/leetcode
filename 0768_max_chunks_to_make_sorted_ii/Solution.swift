// LeetCode 0768 - Max Chunks To Make Sorted II
// https://leetcode.com/problems/max-chunks-to-make-sorted-ii/

class Solution {
    func maxChunksToSorted(_ arr: [Int]) -> Int {
        let n = arr.count
        var maxLeft = arr, minRight = arr
        for i in 1..<n { maxLeft[i] = max(maxLeft[i - 1], arr[i]) }
        for i in stride(from: n - 2, through: 0, by: -1) { minRight[i] = min(minRight[i + 1], arr[i]) }
        var chunks = 1
        for i in 0..<(n - 1) where maxLeft[i] <= minRight[i + 1] { chunks += 1 }
        return chunks
    }
}
