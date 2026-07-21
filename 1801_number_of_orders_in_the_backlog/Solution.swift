// LeetCode 1801 - Number of Orders in the Backlog
// https://leetcode.com/problems/number-of-orders-in-the-backlog/

class Solution {
    func getNumberOfBacklogOrders(_ orders: [[Int]]) -> Int {
        let mod = 1_000_000_007
        var buy: [(Int, Int)] = []
        var sell: [(Int, Int)] = []

        func pushBuy(_ price: Int, _ amount: Int) {
            buy.append((price, amount))
            var i = buy.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if buy[p].0 >= buy[i].0 { break }
                buy.swapAt(p, i)
                i = p
            }
        }
        func popBuy() -> (Int, Int) {
            let top = buy[0]
            let last = buy.removeLast()
            if !buy.isEmpty {
                buy[0] = last
                var i = 0
                while true {
                    var largest = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < buy.count && buy[l].0 > buy[largest].0 { largest = l }
                    if r < buy.count && buy[r].0 > buy[largest].0 { largest = r }
                    if largest == i { break }
                    buy.swapAt(i, largest)
                    i = largest
                }
            }
            return top
        }
        func pushSell(_ price: Int, _ amount: Int) {
            sell.append((price, amount))
            var i = sell.count - 1
            while i > 0 {
                let p = (i - 1) / 2
                if sell[p].0 <= sell[i].0 { break }
                sell.swapAt(p, i)
                i = p
            }
        }
        func popSell() -> (Int, Int) {
            let top = sell[0]
            let last = sell.removeLast()
            if !sell.isEmpty {
                sell[0] = last
                var i = 0
                while true {
                    var smallest = i
                    let l = 2 * i + 1, r = 2 * i + 2
                    if l < sell.count && sell[l].0 < sell[smallest].0 { smallest = l }
                    if r < sell.count && sell[r].0 < sell[smallest].0 { smallest = r }
                    if smallest == i { break }
                    sell.swapAt(i, smallest)
                    i = smallest
                }
            }
            return top
        }

        for order in orders {
            let price = order[0]
            let amount = order[1]
            let orderType = order[2]
            if orderType == 0 {
                pushBuy(price, amount)
            } else {
                pushSell(price, amount)
            }
            while !buy.isEmpty && !sell.isEmpty && buy[0].0 >= sell[0].0 {
                let (bp, ba) = popBuy()
                let (sp, sa) = popSell()
                let matched = min(ba, sa)
                let buyLeft = ba - matched
                let sellLeft = sa - matched
                if buyLeft > 0 { pushBuy(bp, buyLeft) }
                if sellLeft > 0 { pushSell(sp, sellLeft) }
            }
        }

        var total = 0
        for (_, amount) in buy { total = (total + amount) % mod }
        for (_, amount) in sell { total = (total + amount) % mod }
        return total
    }
}
