class FirstUnique {
    count: any;
    queue: any;
    constructor(nums: any) {

        this.count = new Map(); this.queue = [];
        for (const x of nums) this.add(x);
    }
    showFirstUnique(): any {

        while (this.queue.length && this.count.get(this.queue[0]) > 1) this.queue.shift();
        return this.queue.length ? this.queue[0] : -1;
    }
    add(value: any): any {

        this.count.set(value, (this.count.get(value) || 0) + 1);
        if (this.count.get(value) === 1) this.queue.push(value);
    }
}
