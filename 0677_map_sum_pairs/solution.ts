// LeetCode 0677 - Map Sum Pairs
// https://leetcode.com/problems/map-sum-pairs/

export class MapSum {
    constructor() {
    this.values = new Map();
    this.prefixSums = new Map();
}
    insert(key: string, val: number): void {
    const delta = val - (this.values.get(key) || 0);
    this.values.set(key, val);
    for (let i = 1; i <= key.length; ++i) {
        const prefix = key.substring(0, i);
        this.prefixSums.set(prefix, (this.prefixSums.get(prefix) || 0) + delta);
    }
}
    sum(prefix: string): number {
    return this.prefixSums.get(prefix) || 0;
}
}
