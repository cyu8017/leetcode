// LeetCode 0281 - Zigzag Iterator
// https://leetcode.com/problems/zigzag-iterator/

export class ZigzagIterator {
    private vectors: number[][];
    private indices: number[];
    private turn: number;

    constructor(v1: number[], v2: number[]) {
        this.vectors = [v1, v2];
        this.indices = [0, 0];
        this.turn = 0;
    }

    next(): number {
        while (this.indices[this.turn] >= this.vectors[this.turn].length) {
            this.turn = 1 - this.turn;
        }
        const value = this.vectors[this.turn][this.indices[this.turn]];
        this.indices[this.turn] += 1;
        this.turn = 1 - this.turn;
        return value;
    }

    hasNext(): boolean {
        return this.indices.some((index, vectorIndex) => index < this.vectors[vectorIndex].length);
    }
}
