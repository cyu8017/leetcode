// LeetCode 1606 - Find Servers That Handled Most Number of Requests
// https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/

function busiestServers(k: number, arrival: number[], load: number[]): number[] {
    class MinHeap<T> {
        private a: T[] = [];
        constructor(private cmp: (a: T, b: T) => number) {}
        size(): number { return this.a.length; }
        peek(): T { return this.a[0]; }
        push(x: T): void {
            this.a.push(x);
            let i = this.a.length - 1;
            while (i > 0) {
                const p = (i - 1) >> 1;
                if (this.cmp(this.a[p], this.a[i]) <= 0) break;
                [this.a[p], this.a[i]] = [this.a[i], this.a[p]];
                i = p;
            }
        }
        pop(): T {
            const top = this.a[0];
            const last = this.a.pop()!;
            if (!this.a.length) return top;
            this.a[0] = last;
            let i = 0;
            const n = this.a.length;
            while (true) {
                let s = i;
                const l = 2 * i + 1, r = 2 * i + 2;
                if (l < n && this.cmp(this.a[l], this.a[s]) < 0) s = l;
                if (r < n && this.cmp(this.a[r], this.a[s]) < 0) s = r;
                if (s === i) break;
                [this.a[s], this.a[i]] = [this.a[i], this.a[s]];
                i = s;
            }
            return top;
        }
    }

    const free = new MinHeap<number>((a, b) => a - b);
    for (let i = 0; i < k; i++) free.push(i);
    const busy = new MinHeap<[number, number]>((a, b) => a[0] - b[0]);
    const count = Array(k).fill(0);

    for (let i = 0; i < arrival.length; i++) {
        const t = arrival[i];
        while (busy.size() && busy.peek()[0] <= t) {
            const [, server] = busy.pop();
            free.push(i + ((server - i) % k + k) % k);
        }
        if (!free.size()) continue;
        const server = free.pop() % k;
        count[server]++;
        busy.push([t + load[i], server]);
    }
    const best = Math.max(...count);
    const ans: number[] = [];
    for (let i = 0; i < k; i++) if (count[i] === best) ans.push(i);
    return ans;
}
