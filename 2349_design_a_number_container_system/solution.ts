// LeetCode 2349 - Design a Number Container System
// https://leetcode.com/problems/design-a-number-container-system/

export class NumberContainers {
    constructor() {
        this.idx = new Map();
        this.heap = new Map();
    }
    change(index: any, number: any): any {
        this.idx.set(index, number);
        if (!this.heap.has(number)) this.heap.set(number, []);
        this.heap.get(number).push(index);
    }
    find(number: any): any {
        const h = this.heap.get(number);
        if (!h) return -1;
        h.sort((a, b) => a - b);
        while (h.length > 0) {
            const i = h[0];
            if (this.idx.get(i) === number) return i;
            h.shift();
        }
        return -1;
    }
}
