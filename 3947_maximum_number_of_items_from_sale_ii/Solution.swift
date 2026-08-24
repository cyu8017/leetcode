// LeetCode 3947 - Maximum Number of Items From Sale II
// https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/


class Solution {
    func maxItems(_ items: [[Int]], _ budget: Int) -> Int {
        let n = items.count
        var frequency = Array(repeating: 0, count: n + 1)
        var minimumPrice = items[0][1]
        for item in items {
            frequency[item[0]] += 1
            minimumPrice = min(minimumPrice, item[1])
        }
        var batches = [(Int, Int)]()
        for item in items {
            var gain = 0
            var multiple = item[0]
            while multiple <= n {
                gain += frequency[multiple]
                multiple += item[0]
            }
            gain -= 1
            if gain > 0 && item[1] < 2 * minimumPrice {
                batches.append((item[1], gain))
            }
        }
        batches.sort { $0.0 < $1.0 }
        var remaining = budget
        var answer = budget / minimumPrice
        var boosted = 0
        for current in batches {
            var count = current.1
            let affordable = remaining / current.0
            if affordable < count { count = affordable }
            remaining -= count * current.0
            boosted += count
            let total = 2 * boosted + remaining / minimumPrice
            if total > answer { answer = total }
            if count < current.1 { break }
        }
        return answer
    }
}
