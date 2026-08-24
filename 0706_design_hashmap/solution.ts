// LeetCode 0706 - Design HashMap
// https://leetcode.com/problems/design-hashmap/

export class MyHashMap {
    constructor() {
        this.data = new Map();
    }

    put(key: any, value: any): any { this.data.set(key, value); }

    get(key: any): any { return this.data.has(key) ? this.data.get(key) : -1; }

    remove(key: any): any { this.data.delete(key); }
}
