// LeetCode 1418 - Display Table of Food Orders in a Restaurant
// https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

class Solution {
    func displayTable(_ orders: [[String]]) -> [[String]] {
        let foods = Array(Set(orders.map { $0[2] })).sorted()
        let tables = Array(Set(orders.map { Int($0[1])! })).sorted()
        var counts = [String: Int]()
        for o in orders {
            let key = "\(Int(o[1])!)#\(o[2])"
            counts[key, default: 0] += 1
        }
        var result = [["Table"] + foods]
        for table in tables {
            var row = [String(table)]
            for food in foods {
                row.append(String(counts["\(table)#\(food)", default: 0]))
            }
            result.append(row)
        }
        return result
    }
}
