// LeetCode 0381 - Insert Delete GetRandom O(1) - Duplicates allowed
class RandomizedCollection {
    constructor() {
        this.values = [];
        this.indices = new Map();
    }

    insert(val) {
        if (!this.indices.has(val)) {
            this.indices.set(val, new Set());
        }
        this.indices.get(val).add(this.values.length);
        this.values.push(val);
        return this.indices.get(val).size === 1;
    }

    remove(val) {
        if (!this.indices.has(val) || this.indices.get(val).size === 0) {
            return false;
        }

        const index = this.indices.get(val).values().next().value;
        const lastIndex = this.values.length - 1;
        const lastValue = this.values[lastIndex];
        this.values[index] = lastValue;
        this.indices.get(lastValue).delete(lastIndex);
        this.indices.get(lastValue).add(index);
        this.values.pop();
        this.indices.get(val).delete(index);
        if (this.indices.get(val).size === 0) {
            this.indices.delete(val);
        }
        return true;
    }

    getRandom() {
        return this.values[this.values.length - 1];
    }
}

module.exports = { RandomizedCollection };
