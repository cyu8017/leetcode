// LeetCode 2034 - Stock Price Fluctuation
// https://leetcode.com/problems/stock-price-fluctuation/

class StockPrice {
    private var latestTs = 0
    private var priceAt = [Int: Int]()
    private var maxHeap = [(Int, Int)]()
    private var minHeap = [(Int, Int)]()

    init() {}

    func update(_ timestamp: Int, _ price: Int) {
        priceAt[timestamp] = price
        if timestamp >= latestTs { latestTs = timestamp }
        pushMax(price, timestamp)
        pushMin(price, timestamp)
    }

    func current() -> Int {
        return priceAt[latestTs]!
    }

    func maximum() -> Int {
        while true {
            let (p, ts) = maxHeap[0]
            if priceAt[ts] == p { return p }
            popMax()
        }
    }

    func minimum() -> Int {
        while true {
            let (p, ts) = minHeap[0]
            if priceAt[ts] == p { return p }
            popMin()
        }
    }

    private func pushMax(_ p: Int, _ ts: Int) {
        maxHeap.append((p, ts))
        var i = maxHeap.count - 1
        while i > 0 {
            let par = (i - 1) / 2
            if maxHeap[par].0 >= maxHeap[i].0 { break }
            maxHeap.swapAt(par, i)
            i = par
        }
    }

    private func popMax() {
        maxHeap[0] = maxHeap.removeLast()
        if maxHeap.isEmpty { return }
        var i = 0
        while true {
            var best = i
            let l = 2 * i + 1, r = 2 * i + 2
            if l < maxHeap.count && maxHeap[l].0 > maxHeap[best].0 { best = l }
            if r < maxHeap.count && maxHeap[r].0 > maxHeap[best].0 { best = r }
            if best == i { break }
            maxHeap.swapAt(i, best)
            i = best
        }
    }

    private func pushMin(_ p: Int, _ ts: Int) {
        minHeap.append((p, ts))
        var i = minHeap.count - 1
        while i > 0 {
            let par = (i - 1) / 2
            if minHeap[par].0 <= minHeap[i].0 { break }
            minHeap.swapAt(par, i)
            i = par
        }
    }

    private func popMin() {
        minHeap[0] = minHeap.removeLast()
        if minHeap.isEmpty { return }
        var i = 0
        while true {
            var best = i
            let l = 2 * i + 1, r = 2 * i + 2
            if l < minHeap.count && minHeap[l].0 < minHeap[best].0 { best = l }
            if r < minHeap.count && minHeap[r].0 < minHeap[best].0 { best = r }
            if best == i { break }
            minHeap.swapAt(i, best)
            i = best
        }
    }
}
