export class MovingAverage {
    private size: number;
    private values: number[];
    private total: number;

    constructor(size: number) {
        this.size = size;
        this.values = [];
        this.total = 0;
    }

    next(val: number): number {
        this.values.push(val);
        this.total += val;
        if (this.values.length > this.size) {
            this.total -= this.values.shift()!;
        }
        return this.total / this.values.length;
    }
}
