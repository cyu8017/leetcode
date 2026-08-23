// LeetCode 0705 - Design HashSet
// https://leetcode.com/problems/design-hashset/

class MyHashSet {
    constructor() {
        this.data = new Set();
    }

    /**
     * @param {number} key
     * @return {void}
     */
    add(key) { this.data.add(key); }

    /**
     * @param {number} key
     * @return {void}
     */
    remove(key) { this.data.delete(key); }

    /**
     * @param {number} key
     * @return {boolean}
     */
    contains(key) { return this.data.has(key); }
}
