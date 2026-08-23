// LeetCode 0380 - Insert Delete GetRandom O(1)
class RandomizedSet {
    constructor() {
        this.values = [];
        this.indexByValue = new Map();
    }

    insert(val) {
        if (this.indexByValue.has(val)) return false;
        this.indexByValue.set(val, this.values.length);
        this.values.push(val);
        return true;
    }

    remove(val) {
        if (!this.indexByValue.has(val)) return false;
        const index = this.indexByValue.get(val);
        const lastValue = this.values[this.values.length - 1];
        this.values[index] = lastValue;
        this.indexByValue.set(lastValue, index);
        this.values.pop();
        this.indexByValue.delete(val);
        return true;
    }

    getRandom() {
        return this.values[this.values.length - 1];
    }
}

module.exports = { RandomizedSet };
