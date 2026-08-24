// LeetCode 0635 - Design Log Storage System
// https://leetcode.com/problems/design-log-storage-system/

export class LogSystem {
    constructor() {
    this.ids = [];
    this.timestamps = [];
    this.granularityIndex = {
        Year: 4, Month: 7, Day: 10, Hour: 13, Minute: 16, Second: 19
    };
}
    put(id: number, timestamp: string): void {
    this.ids.push(id);
    this.timestamps.push(timestamp);
}
    retrieve(start: string, end: string, granularity: string): number[] {
    const index = this.granularityIndex[granularity];
    const startKey = start.substring(0, index);
    const endKey = end.substring(0, index);
    const matched = [];
    for (let i = 0; i < this.timestamps.length; ++i) {
        const timestamp = this.timestamps[i];
        const key = timestamp.substring(0, index);
        if (startKey <= key && key <= endKey) matched.push([timestamp, this.ids[i]]);
    }
    matched.sort((a, b) => a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : 0);
    return matched.map((item) => item[1]);
}
}
