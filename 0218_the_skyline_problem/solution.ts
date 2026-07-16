// LeetCode 0218 - The Skyline Problem
// https://leetcode.com/problems/the-skyline-problem/

class MinHeap {
    private data: [number, number][] = [];

    size(): number {
        return this.data.length;
    }

    peek(): [number, number] {
        return this.data[0];
    }

    push(item: [number, number]): void {
        this.data.push(item);
        this.siftUp(this.data.length - 1);
    }

    pop(): [number, number] {
        const top = this.data[0];
        const last = this.data.pop()!;
        if (this.data.length > 0) {
            this.data[0] = last;
            this.siftDown(0);
        }
        return top;
    }

    private siftUp(index: number): void {
        while (index > 0) {
            const parent = Math.floor((index - 1) / 2);
            if (this.data[parent][0] <= this.data[index][0]) {
                break;
            }
            [this.data[parent], this.data[index]] = [this.data[index], this.data[parent]];
            index = parent;
        }
    }

    private siftDown(index: number): void {
        const length = this.data.length;
        while (true) {
            let smallest = index;
            const left = index * 2 + 1;
            const right = index * 2 + 2;
            if (left < length && this.data[left][0] < this.data[smallest][0]) {
                smallest = left;
            }
            if (right < length && this.data[right][0] < this.data[smallest][0]) {
                smallest = right;
            }
            if (smallest === index) {
                break;
            }
            [this.data[smallest], this.data[index]] = [this.data[index], this.data[smallest]];
            index = smallest;
        }
    }
}

export function getSkyline(buildings: number[][]): number[][] {
    const events: [number, number, number][] = [];
    for (const [left, right, height] of buildings) {
        events.push([left, -height, right]);
        events.push([right, 0, 0]);
    }
    events.sort((a, b) => a[0] - b[0] || a[1] - b[1]);

    const result: number[][] = [];
    const live = new MinHeap();
    live.push([0, Number.POSITIVE_INFINITY]);

    for (const [x, negH, end] of events) {
        while (live.peek()[1] <= x) {
            live.pop();
        }
        if (negH !== 0) {
            live.push([negH, end]);
        }
        const height = -live.peek()[0];
        if (result.length === 0 || result[result.length - 1][1] !== height) {
            result.push([x, height]);
        }
    }
    return result;
}
