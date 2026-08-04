var FirstUnique = function(nums) {
    this.count = new Map(); this.queue = [];
    for (const x of nums) this.add(x);
};
FirstUnique.prototype.showFirstUnique = function() {
    while (this.queue.length && this.count.get(this.queue[0]) > 1) this.queue.shift();
    return this.queue.length ? this.queue[0] : -1;
};
FirstUnique.prototype.add = function(value) {
    this.count.set(value, (this.count.get(value) || 0) + 1);
    if (this.count.get(value) === 1) this.queue.push(value);
};
