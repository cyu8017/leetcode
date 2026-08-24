// LeetCode 2502 - Design Memory Allocator
// https://leetcode.com/problems/design-memory-allocator/

/**
 * @param {number} n
 */
var Allocator = function(n) {
    this.mem = Array(n).fill(0);
};

/** 
 * @param {number} size 
 * @param {number} mID
 * @return {number}
 */
Allocator.prototype.allocate = function(size, mID) {
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
};

/** 
 * @param {number} mID
 * @return {number}
 */
Allocator.prototype.freeMemory = function(mID) {
    let cnt = 0;
    for (let i = 0; i < this.mem.length; i++) {
        if (this.mem[i] === mID) {
            this.mem[i] = 0;
            cnt++;
        }
    }
    return cnt;
};
