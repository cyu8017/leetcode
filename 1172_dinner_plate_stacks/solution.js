// LeetCode 1172 - Dinner Plate Stacks
// https://leetcode.com/problems/dinner-plate-stacks/

/**
 * @param {number} capacity
 */
var DinnerPlates = function(capacity) {
    this.capacity = capacity;
    this.stacks = [];
    this.available = [];
};

DinnerPlates.prototype._siftUp = function(i) {
    const h = this.available;
    while (i > 0) {
        const p = (i - 1) >> 1;
        if (h[p] <= h[i]) break;
        [h[p], h[i]] = [h[i], h[p]];
        i = p;
    }
};

DinnerPlates.prototype._siftDown = function(i) {
    const h = this.available;
    while (true) {
        let smallest = i;
        const l = 2 * i + 1, r = 2 * i + 2;
        if (l < h.length && h[l] < h[smallest]) smallest = l;
        if (r < h.length && h[r] < h[smallest]) smallest = r;
        if (smallest === i) break;
        [h[i], h[smallest]] = [h[smallest], h[i]];
        i = smallest;
    }
};

DinnerPlates.prototype._pushAvail = function(v) {
    this.available.push(v);
    this._siftUp(this.available.length - 1);
};

DinnerPlates.prototype._popAvail = function() {
    const h = this.available;
    const top = h[0];
    const last = h.pop();
    if (h.length) { h[0] = last; this._siftDown(0); }
    return top;
};

/** 
 * @param {number} val
 * @return {void}
 */
DinnerPlates.prototype.push = function(val) {
    while (this.available.length && (
        this.available[0] >= this.stacks.length ||
        this.stacks[this.available[0]].length === this.capacity
    )) {
        this._popAvail();
    }
    if (!this.available.length) {
        this.stacks.push([]);
        this._pushAvail(this.stacks.length - 1);
    }
    const idx = this.available[0];
    this.stacks[idx].push(val);
    if (this.stacks[idx].length === this.capacity) this._popAvail();
};

/**
 * @return {number}
 */
DinnerPlates.prototype.pop = function() {
    while (this.stacks.length && this.stacks[this.stacks.length - 1].length === 0) {
        this.stacks.pop();
    }
    return this.stacks.length ? this.popAtStack(this.stacks.length - 1) : -1;
};

/** 
 * @param {number} index
 * @return {number}
 */
DinnerPlates.prototype.popAtStack = function(index) {
    if (index < 0 || index >= this.stacks.length || !this.stacks[index].length) return -1;
    if (this.stacks[index].length === this.capacity) this._pushAvail(index);
    return this.stacks[index].pop();
};
