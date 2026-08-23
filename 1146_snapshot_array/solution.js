// LeetCode 1146 - Snapshot Array
// https://leetcode.com/problems/snapshot-array/

/**
 * @param {number} length
 */
var SnapshotArray = function(length) {
    this.snapId = 0;
    this.data = Array.from({ length }, () => [[0, 0]]);
};

/** 
 * @param {number} index 
 * @param {number} val
 * @return {void}
 */
SnapshotArray.prototype.set = function(index, val) {
    const hist = this.data[index];
    if (hist[hist.length - 1][0] === this.snapId) {
        hist[hist.length - 1][1] = val;
    } else {
        hist.push([this.snapId, val]);
    }
};

/**
 * @return {number}
 */
SnapshotArray.prototype.snap = function() {
    this.snapId++;
    return this.snapId - 1;
};

/** 
 * @param {number} index 
 * @param {number} snap_id
 * @return {number}
 */
SnapshotArray.prototype.get = function(index, snap_id) {
    const hist = this.data[index];
    let lo = 0, hi = hist.length - 1, ans = 0;
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        if (hist[mid][0] <= snap_id) {
            ans = mid;
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    return hist[ans][1];
};
