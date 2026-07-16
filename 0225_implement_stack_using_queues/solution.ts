// LeetCode 0225 - Implement Stack using Queues
// https://leetcode.com/problems/implement-stack-using-queues/

export class MyStack {
    private queue: number[] = [];

    push(x: number): null {
        this.queue.push(x);
        for (let i = 0; i < this.queue.length - 1; i += 1) {
            this.queue.push(this.queue.shift()!);
        }
        return null;
    }

    pop(): number {
        return this.queue.shift()!;
    }

    top(): number {
        return this.queue[0];
    }

    empty(): boolean {
        return this.queue.length === 0;
    }
}
