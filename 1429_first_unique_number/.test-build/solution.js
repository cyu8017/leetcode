"use strict";
class FirstUnique {
    constructor(nums) {
        this.count = new Map();
        this.queue = [];
        for (const x of nums)
            this.add(x);
    }
    showFirstUnique() {
        while (this.queue.length && this.count.get(this.queue[0]) > 1)
            this.queue.shift();
        return this.queue.length ? this.queue[0] : -1;
    }
    add(value) {
        this.count.set(value, (this.count.get(value) || 0) + 1);
        if (this.count.get(value) === 1)
            this.queue.push(value);
    }
}
