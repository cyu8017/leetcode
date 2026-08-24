// LeetCode 2502 - Design Memory Allocator
// https://leetcode.com/problems/design-memory-allocator/

export class Allocator {
    constructor(n: number) {
    this.mem = Array(n).fill(0);
}
    allocate(size: number, mID: number): number {
    let freeCnt = 0;
    for (let i = 0; i < this.mem.length; i++) {
        if (this.mem[i] === 0) {
            freeCnt++;
            if (freeCnt === size) {
                const start = i - size + 1;
                for (let j = start; j <= i; j++) this.mem[j] = mID;
                return start;
            }
        } else freeCnt = 0;
    }
    return -1;
}
    freeMemory(mID: number): number {
    let cnt = 0;
    for (let i = 0; i < this.mem.length; i++) {
        if (this.mem[i] === mID) {
            this.mem[i] = 0;
            cnt++;
        }
    }
    return cnt;
}
}
