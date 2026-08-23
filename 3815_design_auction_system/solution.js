// LeetCode 3815 - Design Auction System
// https://leetcode.com/problems/design_auction_system/

function MinHeap(cmp) {
    this.a = [];
    this.cmp = cmp || ((x, y) => x - y);
}
MinHeap.prototype._up = function(i) {
    const a = this.a, cmp = this.cmp;
    while (i > 0) {
        const p = (i - 1) >> 1;
        if (cmp(a[i], a[p]) >= 0) break;
        [a[i], a[p]] = [a[p], a[i]];
        i = p;
    }
};
MinHeap.prototype._down = function(i) {
    const a = this.a, cmp = this.cmp, n = a.length;
    while (true) {
        let s = i, l = i * 2 + 1, r = l + 1;
        if (l < n && cmp(a[l], a[s]) < 0) s = l;
        if (r < n && cmp(a[r], a[s]) < 0) s = r;
        if (s === i) break;
        [a[i], a[s]] = [a[s], a[i]];
        i = s;
    }
};
MinHeap.prototype.push = function(x) { this.a.push(x); this._up(this.a.length - 1); };
MinHeap.prototype.pop = function() {
    const a = this.a;
    if (!a.length) return undefined;
    const top = a[0], last = a.pop();
    if (a.length) { a[0] = last; this._down(0); }
    return top;
};
MinHeap.prototype.peek = function() { return this.a[0]; };
MinHeap.prototype.size = function() { return this.a.length; };
var AuctionSystem = function() {
    this.bids = new Map();
    this.heaps = new Map();
};

AuctionSystem.prototype.addBid = function(userId, itemId, bidAmount) {
    if (!this.bids.has(itemId)) this.bids.set(itemId, new Map());
    this.bids.get(itemId).set(userId, bidAmount);
    if (!this.heaps.has(itemId)) {
        this.heaps.set(itemId, new MinHeap((a, b) => {
            if (a.amount !== b.amount) return b.amount - a.amount;
            return b.userId - a.userId;
        }));
    }
    this.heaps.get(itemId).push({amount: bidAmount, userId: userId});
};

AuctionSystem.prototype.updateBid = function(userId, itemId, newAmount) {
    this.addBid(userId, itemId, newAmount);
};

AuctionSystem.prototype.removeBid = function(userId, itemId) {
    const m = this.bids.get(itemId);
    if (m) m.delete(userId);
};

AuctionSystem.prototype.getHighestBidder = function(itemId) {
    const h = this.heaps.get(itemId);
    if (!h) return -1;
    const m = this.bids.get(itemId) || new Map();
    while (h.size()) {
        const top = h.peek();
        const cur = m.get(top.userId);
        if (cur !== undefined && cur === top.amount) return top.userId;
        h.pop();
    }
    return -1;
};
