// LeetCode 3369 - Design an Array Statistics Tracker
// https://leetcode.com/problems/design-an-array-statistics-tracker/

export class StatisticsTracker {
    constructor() {
    this.arr = [];
    this.sum = 0;
    this.freq = new Map();
    this.modeFreq = 0;
    this.modes = new Set();
}
    addNumber(num: any): any {
    this.arr.push(num);
    this.sum += num;
    const f = (this.freq.get(num) || 0) + 1;
    this.freq.set(num, f);
    if (f > this.modeFreq) {
        this.modeFreq = f;
        this.modes.clear();
        this.modes.add(num);
    } else if (f === this.modeFreq) {
        this.modes.add(num);
    }
}
    removeFirst(): any {
    if (!this.arr.length) return;
    const num = this.arr.shift();
    this.sum -= num;
    const f = this.freq.get(num) - 1;
    if (f === 0) this.freq.delete(num);
    else this.freq.set(num, f);
    this.modeFreq = 0;
    this.modes.clear();
    for (const [v, ff] of this.freq) {
        if (ff > this.modeFreq) {
            this.modeFreq = ff;
            this.modes.clear();
            this.modes.add(v);
        } else if (ff === this.modeFreq) {
            this.modes.add(v);
        }
    }
}
    getMean(): any {
    if (!this.arr.length) return 0;
    return Math.floor(this.sum / this.arr.length);
}
    getMedian(): any {
    const n = this.arr.length;
    const tmp = this.arr.slice().sort((a, b) => a - b);
    if (n % 2 === 1) return tmp[Math.floor(n / 2)];
    return tmp[Math.floor(n / 2) - 1];
}
    getMode(): any {
    let best = Number.MAX_SAFE_INTEGER;
    for (const v of this.modes) if (v < best) best = v;
    if (best === Number.MAX_SAFE_INTEGER) return 0;
    return best;
}
}
