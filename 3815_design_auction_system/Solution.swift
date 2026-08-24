// LeetCode 3815 - Design Auction System
// https://leetcode.com/problems/design-auction-system/

class AuctionSystem {
    private class Bid {
        var amount: Int
        var userId: Int
        init(_ amount: Int, _ userId: Int) {
            self.amount = amount
            self.userId = userId
        }
    }

    private var bids = [Int: [Int: Int]]()
    private var heaps = [Int: [Bid]]()

    init() {}

    func addBid(_ userId: Int, _ itemId: Int, _ bidAmount: Int) {
        if bids[itemId] == nil { bids[itemId] = [:] }
        bids[itemId]![userId] = bidAmount
        if heaps[itemId] == nil { heaps[itemId] = [] }
        heaps[itemId]!.append(Bid(bidAmount, userId))
        heaps[itemId]!.sort { a, b in
            if a.amount != b.amount { return a.amount > b.amount }
            return a.userId > b.userId
        }
    }

    func updateBid(_ userId: Int, _ itemId: Int, _ newAmount: Int) {
        addBid(userId, itemId, newAmount)
    }

    func removeBid(_ userId: Int, _ itemId: Int) {
        bids[itemId]?.removeValue(forKey: userId)
    }

    func getHighestBidder(_ itemId: Int) -> Int {
        guard var h = heaps[itemId] else { return -1 }
        let m = bids[itemId] ?? [:]
        while !h.isEmpty {
            let top = h[0]
            if let cur = m[top.userId], cur == top.amount {
                heaps[itemId] = h
                return top.userId
            }
            h.removeFirst()
        }
        heaps[itemId] = h
        return -1
    }
}
