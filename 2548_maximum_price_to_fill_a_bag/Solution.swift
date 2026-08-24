// LeetCode 2548 - Maximum Price to Fill a Bag
// https://leetcode.com/problems/maximum-price-to-fill-a-bag/

class Solution {
    func maxPrice(_ items: [[Int]], _ capacity: Int) -> Double {
        let items = items.sorted { Double($0[0]) / Double($0[1]) > Double($1[0]) / Double($1[1]) }
        var ans = 0.0
        var remain = capacity
        for it in items {
            let price = it[0], weight = it[1]
            if remain >= weight {
                ans += Double(price)
                remain -= weight
            } else {
                ans += Double(price) * Double(remain) / Double(weight)
                remain = 0
                break
            }
        }
        return remain > 0 ? -1 : ans
    }
}
