// LeetCode 1206 - Design Skiplist
// https://leetcode.com/problems/design-skiplist/

var Skiplist = function() {
    this.values = [];
};

Skiplist.prototype.search = function(target) {
    const i = this._lowerBound(target);
    return i < this.values.length && this.values[i] === target;
};

Skiplist.prototype.add = function(num) {
    const i = this._lowerBound(num);
    this.values.splice(i, 0, num);
};

Skiplist.prototype.erase = function(num) {
    const i = this._lowerBound(num);
    if (i === this.values.length || this.values[i] !== num) {
        return false;
    }
    this.values.splice(i, 1);
    return true;
};

Skiplist.prototype._lowerBound = function(target) {
    let lo = 0;
    let hi = this.values.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (this.values[mid] < target) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }
    return lo;
};
