// LeetCode 0706 - Design HashMap
// https://leetcode.com/problems/design-hashmap/

class MyHashMap {
    constructor() {
        this.data = new Map();
    }

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key, value) { this.data.set(key, value); }

    /**
     * @param {number} key
     * @return {number}
     */
    get(key) { return this.data.has(key) ? this.data.get(key) : -1; }

    /**
     * @param {number} key
     * @return {void}
     */
    remove(key) { this.data.delete(key); }
}
