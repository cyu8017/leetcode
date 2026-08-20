// LeetCode 1481 - Least Number of Unique Integers after K Removals
// https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

class Solution {
    func findLeastNumOfUniqueInts(_ arr: [Int], _ k: Int) -> Int {
        var counts = [Int: Int](), k = k
        for x in arr { counts[x, default: 0] += 1 }
        var removed = 0
        for count in counts.values.sorted() {
            if k < count { break }
            k -= count; removed += 1
        }
        return counts.count - removed
    }
}
