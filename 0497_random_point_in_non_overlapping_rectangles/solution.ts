// LeetCode 0497 - Random Point in Non-overlapping Rectangles
// https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

let uniform: (a: number, b: number) => number = () => 0;

export function set_uniform(uniformFn: (a: number, b: number) => number): void {
    uniform = uniformFn;
}

export function setUniform(uniformFn: (a: number, b: number) => number): void {
    uniform = uniformFn;
}

export class Solution {
    private rects: number[][];
    private total: number;

    constructor(rects: number[][]) {
        this.rects = rects;
        let total = 0;
        for (const [a, b, x, y] of rects) {
            total += (x - a + 1) * (y - b + 1);
        }
        this.total = total;
    }

    pick(): number[] {
        let index = Math.trunc(uniform(0, this.total));
        if (index >= this.total) index = this.total - 1;
        for (const [a, b, x, y] of this.rects) {
            const width = x - a + 1;
            const height = y - b + 1;
            const size = width * height;
            if (index < size) {
                const offsetX = index % width;
                const offsetY = Math.floor(index / width);
                return [a + offsetX, b + offsetY];
            }
            index -= size;
        }
        const last = this.rects[this.rects.length - 1];
        return [last[0], last[1]];
    }
}
