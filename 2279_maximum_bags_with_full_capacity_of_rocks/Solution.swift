// LeetCode 2279 - Maximum Bags With Full Capacity of Rocks
// https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

class Solution {
    func maximumBags(_ capacity: [Int], _ rocks: [Int], _ additionalRocks: Int) -> Int {
        var need = zip(capacity, rocks).map { $0 - $1 }.sorted()
        var extra = additionalRocks, ans = 0
        for n in need {
            if extra < n { break }
            extra -= n
            ans += 1
        }
        return ans
    }
}
