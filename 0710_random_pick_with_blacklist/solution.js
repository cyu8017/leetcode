// LeetCode 0710 - Random Pick with Blacklist
// https://leetcode.com/problems/random-pick-with-blacklist/

class Solution {
    /**
     * @param {number} n
     * @param {number[]} blacklist
     */
    constructor(n, blacklist) {
        this.size = n - blacklist.length;
        this.mapping = new Map();
        const black = new Set(blacklist);
        let white = this.size;
        for (const b of blacklist) {
            if (b < this.size) {
                while (black.has(white)) white++;
                this.mapping.set(b, white++);
            }
        }
    }

    /**
     * @return {number}
     */
    pick() {
        const index = Math.floor(Math.random() * this.size);
        return this.mapping.has(index) ? this.mapping.get(index) : index;
    }
}
