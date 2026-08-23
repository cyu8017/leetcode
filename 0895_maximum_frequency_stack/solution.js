// LeetCode 0895 - Maximum Frequency Stack
// https://leetcode.com/problems/maximum-frequency-stack/

class FreqStack {
    constructor() {
        this.freq = new Map();
        this.group = new Map();
        this.maxfreq = 0;
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        const f = (this.freq.get(val) || 0) + 1;
        this.freq.set(val, f);
        this.maxfreq = Math.max(this.maxfreq, f);
        if (!this.group.has(f)) this.group.set(f, []);
        this.group.get(f).push(val);
    }

    /**
     * @return {number}
     */
    pop() {
        const list = this.group.get(this.maxfreq);
        const val = list.pop();
        this.freq.set(val, this.freq.get(val) - 1);
        if (list.length === 0) this.maxfreq--;
        return val;
    }
}

module.exports = { FreqStack };
