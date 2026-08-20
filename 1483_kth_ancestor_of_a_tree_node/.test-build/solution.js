"use strict";
class TreeAncestor {
    constructor(n, parent) {
        this.up = [parent.slice()];
        const width = Math.max(1, Math.ceil(Math.log2(Math.max(2, n))) + 1);
        for (let bit = 1; bit < width; bit++) {
            const previous = this.up[bit - 1];
            this.up.push(previous.map((node) => node === -1 ? -1 : previous[node]));
        }
    }
    getKthAncestor(node, k) {
        let bit = 0;
        while (k && node !== -1) {
            if (k & 1) {
                if (bit === this.up.length)
                    return -1;
                node = this.up[bit][node];
            }
            k >>= 1;
            bit++;
        }
        return node;
    }
}
