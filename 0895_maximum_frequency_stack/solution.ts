// LeetCode 0895 - Maximum Frequency Stack
// https://leetcode.com/problems/maximum-frequency-stack/

export class FreqStack {
    constructor() {
        this.freq = new Map();
        this.group = new Map();
        this.maxfreq = 0;
    }

    push(val: any): any {
        const f = (this.freq.get(val) || 0) + 1;
        this.freq.set(val, f);
        this.maxfreq = Math.max(this.maxfreq, f);
        if (!this.group.has(f)) this.group.set(f, []);
        this.group.get(f).push(val);
    }

    pop(): any {
        const list = this.group.get(this.maxfreq);
        const val = list.pop();
        this.freq.set(val, this.freq.get(val) - 1);
        if (list.length === 0) this.maxfreq--;
        return val;
    }
}
