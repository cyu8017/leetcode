// LeetCode 0710 - Random Pick with Blacklist
// https://leetcode.com/problems/random-pick-with-blacklist/

export class Solution {
    constructor(n: any, blacklist: any) {
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

    pick(): any {
        const index = Math.floor(Math.random() * this.size);
        return this.mapping.has(index) ? this.mapping.get(index) : index;
    }
}
