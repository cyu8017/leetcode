// LeetCode 0381 - Insert Delete GetRandom O(1) - Duplicates allowed
export class RandomizedCollection {
    private values: number[];
    private indices: Map<number, Set<number>>;

    constructor() {
        this.values = [];
        this.indices = new Map();
    }

    insert(val: number): boolean {
        if (!this.indices.has(val)) {
            this.indices.set(val, new Set());
        }
        this.indices.get(val)!.add(this.values.length);
        this.values.push(val);
        return this.indices.get(val)!.size === 1;
    }

    remove(val: number): boolean {
        const indexSet = this.indices.get(val);
        if (!indexSet || indexSet.size === 0) return false;

        const index = indexSet.values().next().value as number;
        const lastIndex = this.values.length - 1;
        const lastValue = this.values[lastIndex];
        this.values[index] = lastValue;
        this.indices.get(lastValue)!.delete(lastIndex);
        this.indices.get(lastValue)!.add(index);
        this.values.pop();
        indexSet.delete(index);
        if (indexSet.size === 0) this.indices.delete(val);
        return true;
    }

    getRandom(): number {
        return this.values[this.values.length - 1];
    }
}
