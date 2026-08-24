// LeetCode 2070 - Most Beautiful Item for Each Query
// https://leetcode.com/problems/most-beautiful-item-for-each-query/

class Solution {
    func maximumBeauty(_ items: [[Int]], _ queries: [Int]) -> [Int] {
        var items = items.sorted { $0[0] < $1[0] }
        var maxB = 0
        for i in 0..<items.count {
            maxB = max(maxB, items[i][1])
            items[i][1] = maxB
        }
        return queries.map { q in
            var lo = 0, hi = items.count
            while lo < hi {
                let mid = (lo + hi) / 2
                if items[mid][0] <= q { lo = mid + 1 }
                else { hi = mid }
            }
            return lo == 0 ? 0 : items[lo - 1][1]
        }
    }
}
