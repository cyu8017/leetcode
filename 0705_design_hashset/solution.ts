// LeetCode 0705 - Design HashSet
// https://leetcode.com/problems/design-hashset/

export class MyHashSet {
    constructor() {
        this.data = new Set();
    }

    add(key: any): any { this.data.add(key); }

    remove(key: any): any { this.data.delete(key); }

    contains(key: any): any { return this.data.has(key); }
}
