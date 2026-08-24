// LeetCode 3508 - Implement Router
// https://leetcode.com/problems/implement-router/

export class Router {
    constructor(memoryLimit: any) {
    this.lim = memoryLimit;
    this.vis = new Set();
    this.q = [];
    this.idx = new Map();
    this.d = new Map();
}
    f(a: any, b: any, c: any): any {
    return (BigInt(a) << 46n) | (BigInt(b) << 29n) | BigInt(c);
}
    addPacket(source: any, destination: any, timestamp: any): any {
    const x = this.f(source, destination, timestamp);
    if (this.vis.has(x)) return false;
    this.vis.add(x);
    if (this.q.length >= this.lim) this.forwardPacket();
    this.q.push([source, destination, timestamp]);
    if (!this.d.has(destination)) this.d.set(destination, []);
    this.d.get(destination).push(timestamp);
    return true;
}
    forwardPacket(): any {
    if (this.q.length === 0) return [];
    const packet = this.q.shift();
    const s = packet[0], dest = packet[1], t = packet[2];
    this.vis.delete(this.f(s, dest, t));
    this.idx.set(dest, (this.idx.get(dest) || 0) + 1);
    return [s, dest, t];
}
    getCount(destination: any, startTime: any, endTime: any): any {
    const ls = this.d.get(destination);
    if (!ls) return 0;
    const k = this.idx.get(destination) || 0;
    return lowerBound(ls, k, endTime + 1) - lowerBound(ls, k, startTime);
}
}

function lowerBound(a: any, from: any, target: any): any {
    let lo = from, hi = a.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (a[mid] < target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}
