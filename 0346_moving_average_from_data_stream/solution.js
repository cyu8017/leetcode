// LeetCode 0346 - Moving Average from Data Stream
class MovingAverage {
    constructor(size) {
        this.size = size;
        this.values = [];
        this.total = 0;
    }

    next(val) {
        this.values.push(val);
        this.total += val;
        if (this.values.length > this.size) {
            this.total -= this.values.shift();
        }
        return this.total / this.values.length;
    }
}

module.exports = { MovingAverage };
