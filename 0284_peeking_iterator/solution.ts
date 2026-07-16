// LeetCode 0284 - Peeking Iterator
// https://leetcode.com/problems/peeking-iterator/

interface NumberIterator {
    next(): number;
    hasNext(): boolean;
}

export class PeekingIterator {
    private iterator: NumberIterator;
    private peeked: number | null;
    private hasPeeked: boolean;

    constructor(iterator: NumberIterator) {
        this.iterator = iterator;
        this.peeked = null;
        this.hasPeeked = false;
    }

    peek(): number {
        if (!this.hasPeeked) {
            this.peeked = this.iterator.next();
            this.hasPeeked = true;
        }
        return this.peeked as number;
    }

    next(): number {
        if (this.hasPeeked) {
            const result = this.peeked as number;
            this.peeked = null;
            this.hasPeeked = false;
            return result;
        }
        return this.iterator.next();
    }

    hasNext(): boolean {
        return this.hasPeeked || this.iterator.hasNext();
    }
}
