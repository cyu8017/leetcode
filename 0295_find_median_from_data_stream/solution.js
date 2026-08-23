// LeetCode 0295 - Find Median from Data Stream
// https://leetcode.com/problems/find-median-from-data-stream/

class MinHeap {
    constructor() {
        this.data = [];
    }

    push(value) {
        this.data.push(value);
        this.bubbleUp(this.data.length - 1);
    }

    pop() {
        const top = this.data[0];
        const last = this.data.pop();
        if (this.data.length > 0) {
            this.data[0] = last;
            this.bubbleDown(0);
        }
        return top;
    }

    peek() {
        return this.data[0];
    }

    get size() {
        return this.data.length;
    }

    bubbleUp(index) {
        while (index > 0) {
            const parent = Math.floor((index - 1) / 2);
            if (this.data[index] >= this.data[parent]) {
                break;
            }
            [this.data[index], this.data[parent]] = [this.data[parent], this.data[index]];
            index = parent;
        }
    }

    bubbleDown(index) {
        while (true) {
            let target = index;
            const left = index * 2 + 1;
            const right = left + 1;
            if (left < this.data.length && this.data[left] < this.data[target]) {
                target = left;
            }
            if (right < this.data.length && this.data[right] < this.data[target]) {
                target = right;
            }
            if (target === index) {
                break;
            }
            [this.data[index], this.data[target]] = [this.data[target], this.data[index]];
            index = target;
        }
    }
}

class MaxHeap {
    constructor() {
        this.heap = new MinHeap();
    }

    push(value) {
        this.heap.push(-value);
    }

    pop() {
        return -this.heap.pop();
    }

    peek() {
        return -this.heap.peek();
    }

    get size() {
        return this.heap.size;
    }
}

class MedianFinder {
    constructor() {
        this.small = new MaxHeap();
        this.large = new MinHeap();
    }

    /**
     * @param {number} num
     * @return {void}
     */
    addNum(num) {
        this.small.push(num);
        this.large.push(this.small.pop());
        if (this.large.size > this.small.size) {
            this.small.push(this.large.pop());
        }
    }

    /**
     * @return {number}
     */
    findMedian() {
        if (this.small.size > this.large.size) {
            return this.small.peek();
        }
        return (this.small.peek() + this.large.peek()) / 2;
    }
}

module.exports = { MedianFinder };
