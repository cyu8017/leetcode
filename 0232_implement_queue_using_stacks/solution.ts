// LeetCode 0232 - Implement Queue using Stacks
// https://leetcode.com/problems/implement-queue-using-stacks/

export class MyQueue {
    private inputStack: number[] = [];
    private outputStack: number[] = [];

    private move(): void {
        if (this.outputStack.length === 0) {
            while (this.inputStack.length > 0) {
                this.outputStack.push(this.inputStack.pop()!);
            }
        }
    }

    push(x: number): null {
        this.inputStack.push(x);
        return null;
    }

    pop(): number {
        this.move();
        return this.outputStack.pop()!;
    }

    peek(): number {
        this.move();
        return this.outputStack[this.outputStack.length - 1];
    }

    empty(): boolean {
        return this.inputStack.length === 0 && this.outputStack.length === 0;
    }
}
