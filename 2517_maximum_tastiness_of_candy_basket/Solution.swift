// LeetCode 2517 - Maximum Tastiness of Candy Basket
// https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

class Solution {
    func maximumTastiness(_ price: [Int], _ k: Int) -> Int {
        let price = price.sorted()
        func ok(_ d: Int) -> Bool {
            var cnt = 1, last = price[0]
            for i in 1..<price.count {
                if price[i] - last >= d {
                    cnt += 1
                    last = price[i]
                    if cnt >= k { return true }
                }
            }
            return false
        }
        var lo = 0, hi = price[price.count - 1] - price[0]
        while lo < hi {
            let mid = (lo + hi + 1) / 2
            if ok(mid) { lo = mid } else { hi = mid - 1 }
        }
        return lo
    }
}
