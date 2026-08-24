// LeetCode 3815 - Design Auction System
// https://leetcode.com/problems/design_auction_system/

export class AuctionSystem {
    constructor() {
    this.bids = new Map();
    this.heaps = new Map();
}
    addBid(userId: any, itemId: any, bidAmount: any): any {
    if (!this.bids.has(itemId)) this.bids.set(itemId, new Map());
    this.bids.get(itemId).set(userId, bidAmount);
    if (!this.heaps.has(itemId)) {
        this.heaps.set(itemId, new MinHeap((a, b) => {
            if (a.amount !== b.amount) return b.amount - a.amount;
            return b.userId - a.userId;
        }));
    }
    this.heaps.get(itemId).push({amount: bidAmount, userId: userId});
}
    updateBid(userId: any, itemId: any, newAmount: any): any {
    this.addBid(userId, itemId, newAmount);
}
    removeBid(userId: any, itemId: any): any {
    const m = this.bids.get(itemId);
    if (m) m.delete(userId);
}
    getHighestBidder(itemId: any): any {
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
}
}

export class MinHeap {
    constructor(cmp: any) {
    this.a = [];
    this.cmp = cmp || ((x, y) => x - y);
}
    _up(i: any): any {
    const a = this.a, cmp = this.cmp;
    while (i > 0) {
        const p = (i - 1) >> 1;
        if (cmp(a[i], a[p]) >= 0) break;
        [a[i], a[p]] = [a[p], a[i]];
        i = p;
    }
}
    _down(i: any): any {
    const a = this.a, cmp = this.cmp, n = a.length;
    while (true) {
        let s = i, l = i * 2 + 1, r = l + 1;
        if (l < n && cmp(a[l], a[s]) < 0) s = l;
        if (r < n && cmp(a[r], a[s]) < 0) s = r;
        if (s === i) break;
        [a[i], a[s]] = [a[s], a[i]];
        i = s;
    }
}
    push(x: any): any { this.a.push(x); this._up(this.a.length - 1); }
    pop(): any {
    const a = this.a;
    if (!a.length) return undefined;
    const top = a[0], last = a.pop();
    if (a.length) { a[0] = last; this._down(0); }
    return top;
}
    peek(): any { return this.a[0]; }
    size(): any { return this.a.length; }
}
