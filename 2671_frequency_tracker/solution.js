// LeetCode 2671 - Frequency Tracker
// https://leetcode.com/problems/frequency-tracker/

var FrequencyTracker = function() {
    this.freq = new Map();
    this.count = new Map();
};

FrequencyTracker.prototype.add = function(number) {
    const old = this.freq.get(number) || 0;
    if (old > 0) this.count.set(old, (this.count.get(old) || 0) - 1);
    this.freq.set(number, old + 1);
    this.count.set(old + 1, (this.count.get(old + 1) || 0) + 1);
};

FrequencyTracker.prototype.deleteOne = function(number) {
    const old = this.freq.get(number) || 0;
    if (old === 0) return;
    this.count.set(old, (this.count.get(old) || 0) - 1);
    this.freq.set(number, old - 1);
    if (old - 1 > 0) this.count.set(old - 1, (this.count.get(old - 1) || 0) + 1);
};

FrequencyTracker.prototype.hasFrequency = function(frequency) {
    return (this.count.get(frequency) || 0) > 0;
};
