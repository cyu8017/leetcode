// LeetCode 2166 - Design Bitset
// https://leetcode.com/problems/design-bitset/

export class Bitset {
    constructor(size: any) {
        this.size = size;
        this.bits = new Array(size).fill(0);
        this.ones = 0;
        this.flipped = false;
    }

    fix(idx: any): any {
        const target = this.flipped ? 0 : 1;
        if (this.bits[idx] !== target) {
            this.bits[idx] = target;
            this.ones += this.flipped ? -1 : 1;
        }
    }

    unfix(idx: any): any {
        const target = this.flipped ? 1 : 0;
        if (this.bits[idx] !== target) {
            this.bits[idx] = target;
            this.ones += this.flipped ? 1 : -1;
        }
    }

    flip(): any {
        this.flipped = !this.flipped;
        this.ones = this.size - this.ones;
    }

    all(): any { return this.ones === this.size; }

    one(): any { return this.ones > 0; }

    count(): any { return this.ones; }

    toString(): any {
        const b = new Array(this.size);
        for (let i = 0; i < this.size; i++) {
            let v = this.bits[i];
            if (this.flipped) v ^= 1;
            b[i] = String(v);
        }
        return b.join('');
    }
}
