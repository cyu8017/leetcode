// LeetCode 0460 - LFU Cache
// https://leetcode.com/problems/lfu-cache/

class LFUCache {
    constructor(capacity) {
        this.capacity = capacity;
        this.minFreq = 0;
        this.keyValues = new Map();
        this.keyFreqs = new Map();
        this.freqKeys = new Map();
    }

    _touch(key) {
        const freq = this.keyFreqs.get(key);
        const bucket = this.freqKeys.get(freq);
        const index = bucket.indexOf(key);
        bucket.splice(index, 1);
        if (!bucket.length && freq === this.minFreq) {
            this.minFreq += 1;
        }
        const nextFreq = freq + 1;
        this.keyFreqs.set(key, nextFreq);
        if (!this.freqKeys.has(nextFreq)) {
            this.freqKeys.set(nextFreq, []);
        }
        this.freqKeys.get(nextFreq).push(key);
    }

    get(key) {
        if (!this.keyValues.has(key)) return -1;
        this._touch(key);
        return this.keyValues.get(key);
    }

    put(key, value) {
        if (this.capacity === 0) return;
        if (this.keyValues.has(key)) {
            this.keyValues.set(key, value);
            this._touch(key);
            return;
        }

        if (this.keyValues.size >= this.capacity) {
            const evict = this.freqKeys.get(this.minFreq).shift();
            this.keyValues.delete(evict);
            this.keyFreqs.delete(evict);
        }

        this.keyValues.set(key, value);
        this.keyFreqs.set(key, 1);
        if (!this.freqKeys.has(1)) {
            this.freqKeys.set(1, []);
        }
        this.freqKeys.get(1).push(key);
        this.minFreq = 1;
    }
}

module.exports = { LFUCache };
