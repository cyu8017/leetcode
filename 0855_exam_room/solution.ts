// LeetCode 0855 - Exam Room
// https://leetcode.com/problems/exam-room/

export class ExamRoom {
    constructor(n: number) {
    this.n = n;
    this.seats = [];
}
    seat(): number {
    if (!this.seats.length) {
        this.seats.push(0);
        return 0;
    }
    let bestSeat = 0;
    let bestDist = this.seats[0];
    let prev = this.seats[0];
    for (const cur of this.seats) {
        if (cur === prev) continue;
        const dist = Math.floor((cur - prev) / 2);
        if (dist > bestDist) {
            bestDist = dist;
            bestSeat = prev + dist;
        }
        prev = cur;
    }
    if (this.n - 1 - this.seats[this.seats.length - 1] > bestDist) bestSeat = this.n - 1;
    this.seats.push(bestSeat);
    this.seats.sort((a, b) => a - b);
    return bestSeat;
}
    leave(p: number): void {
    const idx = this.seats.indexOf(p);
    if (idx >= 0) this.seats.splice(idx, 1);
}
}
