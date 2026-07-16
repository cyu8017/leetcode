// LeetCode 0251 - Flatten 2D Vector
// https://leetcode.com/problems/flatten-2d-vector/

export class Vector2D {
    private readonly vec: number[][];
    private row = 0;
    private col = 0;

    constructor(vec: number[][]) {
        this.vec = vec;
        this.advance();
    }

    private advance(): void {
        while (this.row < this.vec.length && this.col >= this.vec[this.row].length) {
            this.row += 1;
            this.col = 0;
        }
    }

    next(): number {
        const value = this.vec[this.row][this.col];
        this.col += 1;
        this.advance();
        return value;
    }

    hasNext(): boolean {
        this.advance();
        return this.row < this.vec.length;
    }
}
