// LeetCode 0769 - Max Chunks To Make Sorted
// https://leetcode.com/problems/max-chunks-to-make-sorted/

class Solution {
    func maxChunksToSorted(_ arr: [Int]) -> Int {
        var mx = 0, chunks = 0
        for i in 0..<arr.count {
            mx = max(mx, arr[i])
            if mx == i { chunks += 1 }
        }
        return chunks
    }
}
