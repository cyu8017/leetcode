// LeetCode 0900 - RLE Iterator
// https://leetcode.com/problems/rle-iterator/

export class RLEIterator {
    constructor(encoding: any) {
        this.enc = encoding.slice();
        this.i = 0;
    }

    next(n: any): any {
        while (this.i < this.enc.length) {
            if (this.enc[this.i] >= n) {
                this.enc[this.i] -= n;
                return this.enc[this.i + 1];
            }
            n -= this.enc[this.i];
            this.i += 2;
        }
        return -1;
    }
}
