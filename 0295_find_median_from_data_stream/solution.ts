// LeetCode 0295 - Find Median from Data Stream
// https://leetcode.com/problems/find-median-from-data-stream/

export class MedianFinder {
    private small: number[];
    private large: number[];

    constructor() {
        this.small = [];
        this.large = [];
    }

    addNum(num: number): void {
        this.push(this.small, -num, true);
        this.push(this.large, -this.pop(this.small), false);
        if (this.large.length > this.small.length) {
            this.push(this.small, -this.pop(this.large), true);
        }
    }

    findMedian(): number {
        if (this.small.length > this.large.length) {
            return -this.small[0];
        }
        return (-this.small[0] + this.large[0]) / 2;
    }

    private push(heap: number[], value: number, isMaxHeap: boolean): void {
        heap.push(value);
        this.bubbleUp(heap, heap.length - 1, isMaxHeap);
    }

    private pop(heap: number[]): number {
        const top = heap[0];
        const last = heap.pop() as number;
        if (heap.length > 0) {
            heap[0] = last;
            this.bubbleDown(heap, 0, heap === this.small);
        }
        return top;
    }

    private bubbleUp(heap: number[], index: number, isMaxHeap: boolean): void {
        while (index > 0) {
            const parent = Math.floor((index - 1) / 2);
            if (isMaxHeap ? heap[index] <= heap[parent] : heap[index] >= heap[parent]) {
                break;
            }
            [heap[index], heap[parent]] = [heap[parent], heap[index]];
            index = parent;
        }
    }

    private bubbleDown(heap: number[], index: number, isMaxHeap: boolean): void {
        while (true) {
            let target = index;
            const left = index * 2 + 1;
            const right = left + 1;
            if (left < heap.length && (isMaxHeap ? heap[left] > heap[target] : heap[left] < heap[target])) {
                target = left;
            }
            if (right < heap.length && (isMaxHeap ? heap[right] > heap[target] : heap[right] < heap[target])) {
                target = right;
            }
            if (target === index) {
                break;
            }
            [heap[index], heap[target]] = [heap[target], heap[index]];
            index = target;
        }
    }
}
