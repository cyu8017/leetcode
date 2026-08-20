// LeetCode 1206 - Design Skiplist
// https://leetcode.com/problems/design-skiplist/

class Skiplist {
    values: any;

    constructor() {
        this.values = [];
    }

    search(target: any): any {
        const i = this._lowerBound(target);
        return i < this.values.length && this.values[i] === target;
    }

    add(num: any): any {
        const i = this._lowerBound(num);
        this.values.splice(i, 0, num);
    }

    erase(num: any): any {
        const i = this._lowerBound(num);
        if (i === this.values.length || this.values[i] !== num) {
            return false;
        }
        this.values.splice(i, 1);
        return true;
    }

    _lowerBound(target: any): any {
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
    }
}
