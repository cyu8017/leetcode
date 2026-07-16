export class RandomizedSet {
    private values: number[];
    private indexByValue: Map<number, number>;

    constructor() {
        this.values = [];
        this.indexByValue = new Map();
    }

    insert(val: number): boolean {
        if (this.indexByValue.has(val)) return false;
        this.indexByValue.set(val, this.values.length);
        this.values.push(val);
        return true;
    }

    remove(val: number): boolean {
        if (!this.indexByValue.has(val)) return false;
        const index = this.indexByValue.get(val)!;
        const lastValue = this.values[this.values.length - 1];
        this.values[index] = lastValue;
        this.indexByValue.set(lastValue, index);
        this.values.pop();
        this.indexByValue.delete(val);
        return true;
    }

    getRandom(): number {
        return this.values[this.values.length - 1];
    }
}
