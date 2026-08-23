// LeetCode 3508 - Implement Router
// https://leetcode.com/problems/implement-router/

var Router = function(memoryLimit) {
    this.lim = memoryLimit;
    this.vis = new Set();
    this.q = [];
    this.idx = new Map();
    this.d = new Map();
};

Router.prototype.f = function(a, b, c) {
    return (BigInt(a) << 46n) | (BigInt(b) << 29n) | BigInt(c);
};

Router.prototype.addPacket = function(source, destination, timestamp) {
    const x = this.f(source, destination, timestamp);
    if (this.vis.has(x)) return false;
    this.vis.add(x);
    if (this.q.length >= this.lim) this.forwardPacket();
    this.q.push([source, destination, timestamp]);
    if (!this.d.has(destination)) this.d.set(destination, []);
    this.d.get(destination).push(timestamp);
    return true;
};

Router.prototype.forwardPacket = function() {
    if (this.q.length === 0) return [];
    const packet = this.q.shift();
    const s = packet[0], dest = packet[1], t = packet[2];
    this.vis.delete(this.f(s, dest, t));
    this.idx.set(dest, (this.idx.get(dest) || 0) + 1);
    return [s, dest, t];
};

Router.prototype.getCount = function(destination, startTime, endTime) {
    const ls = this.d.get(destination);
    if (!ls) return 0;
    const k = this.idx.get(destination) || 0;
    return lowerBound(ls, k, endTime + 1) - lowerBound(ls, k, startTime);
};

function lowerBound(a, from, target) {
    let lo = from, hi = a.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (a[mid] < target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}
