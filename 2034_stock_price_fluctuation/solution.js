// LeetCode 2034 - Stock Price Fluctuation
// https://leetcode.com/problems/stock-price-fluctuation/

class StockPrice {
    constructor() {
        this.latestTs = 0;
        this.priceAt = new Map();
        this.maxHeap = [];
        this.minHeap = [];
    }

    _pushMax(item) {
        this.maxHeap.push(item);
        this.maxHeap.sort((a, b) => b[0] - a[0]);
    }
    _pushMin(item) {
        this.minHeap.push(item);
        this.minHeap.sort((a, b) => a[0] - b[0]);
    }

    /**
     * @param {number} timestamp
     * @param {number} price
     * @return {void}
     */
    update(timestamp, price) {
        this.priceAt.set(timestamp, price);
        if (timestamp >= this.latestTs) this.latestTs = timestamp;
        this._pushMax([price, timestamp]);
        this._pushMin([price, timestamp]);
    }

    /**
     * @return {number}
     */
    current() {
        return this.priceAt.get(this.latestTs);
    }

    /**
     * @return {number}
     */
    maximum() {
        while (true) {
            const top = this.maxHeap[0];
            if (this.priceAt.get(top[1]) === top[0]) return top[0];
            this.maxHeap.shift();
        }
    }

    /**
     * @return {number}
     */
    minimum() {
        while (true) {
            const top = this.minHeap[0];
            if (this.priceAt.get(top[1]) === top[0]) return top[0];
            this.minHeap.shift();
        }
    }
}
