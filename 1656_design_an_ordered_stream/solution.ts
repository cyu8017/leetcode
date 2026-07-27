// LeetCode 1656 - Design an Ordered Stream
// https://leetcode.com/problems/design-an-ordered-stream/

export class OrderedStream {
    private a: (string | null)[];
    private p: number;

    constructor(n: number) {
        this.a = Array(n + 1).fill(null);
        this.p = 1;
    }

    insert(idKey: number, value: string): string[] {
        this.a[idKey] = value;
        const out: string[] = [];
        while (this.p < this.a.length && this.a[this.p] !== null) {
            out.push(this.a[this.p]!);
            this.p++;
        }
        return out;
    }
}
