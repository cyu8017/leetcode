// LeetCode 2336 - Smallest Number in Infinite Set
// https://leetcode.com/problems/smallest-number-in-infinite-set/

class SmallestInfiniteSet {
    constructor() {
        this.next = 1;
        this.added = new Set();
        this.heap = [];
    }
    _bubbleUp(i) {
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (this.heap[p] <= this.heap[i]) break;
            [this.heap[p], this.heap[i]] = [this.heap[i], this.heap[p]];
            i = p;
        }
    }
    _bubbleDown(i) {
        const n = this.heap.length;
        while (true) {
            let smallest = i;
            const l = i * 2 + 1, r = i * 2 + 2;
            if (l < n && this.heap[l] < this.heap[smallest]) smallest = l;
            if (r < n && this.heap[r] < this.heap[smallest]) smallest = r;
            if (smallest === i) break;
            [this.heap[smallest], this.heap[i]] = [this.heap[i], this.heap[smallest]];
            i = smallest;
        }
    }
    _push(x) {
        this.heap.push(x);
        this._bubbleUp(this.heap.length - 1);
    }
    _pop() {
        const top = this.heap[0];
        const last = this.heap.pop();
        if (this.heap.length > 0) {
            this.heap[0] = last;
            this._bubbleDown(0);
        }
        return top;
    }
    popSmallest() {
        if (this.heap.length > 0) {
            const x = this._pop();
            this.added.delete(x);
            return x;
        }
        return this.next++;
    }
    addBack(num) {
        if (num < this.next && !this.added.has(num)) {
            this.added.add(num);
            this._push(num);
        }
    }
}
