// LeetCode 2526 - Find Consecutive Integers from a Data Stream
// https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

export class DataStream {
    constructor(value: number, k: number) {
    this.value = value;
    this.k = k;
    this.streak = 0;
}
    consec(num: number): boolean {
    if (num === this.value) this.streak++;
    else this.streak = 0;
    return this.streak >= this.k;
}
}
