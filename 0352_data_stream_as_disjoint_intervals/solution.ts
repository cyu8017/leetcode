export class SummaryRanges {
    private intervals: number[][];

    constructor() {
        this.intervals = [];
    }

    addNum(value: number): void {
        const newInterval = [value, value];
        const merged: number[][] = [];
        let inserted = false;

        for (const interval of this.intervals) {
            if (interval[1] < value - 1) merged.push(interval);
            else if (interval[0] > value + 1) {
                if (!inserted) {
                    merged.push(newInterval);
                    inserted = true;
                }
                merged.push(interval);
            } else {
                newInterval[0] = Math.min(newInterval[0], interval[0]);
                newInterval[1] = Math.max(newInterval[1], interval[1]);
            }
        }

        if (!inserted) merged.push(newInterval);
        this.intervals = merged;
    }

    getIntervals(): number[][] {
        return this.intervals;
    }
}
