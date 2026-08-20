// LeetCode 1338 - Reduce Array Size to The Half
// https://leetcode.com/problems/reduce-array-size-to-the-half/

class Solution {
    func minSetSize(_ arr: [Int]) -> Int {
        var counts = [Int: Int]()
        for x in arr { counts[x, default: 0] += 1 }
        var removed = 0, size = 0
        for frequency in counts.values.sorted(by: >) {
            removed += frequency
            size += 1
            if removed * 2 >= arr.count { return size }
        }
        return size
    }
}
