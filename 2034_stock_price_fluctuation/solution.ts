// LeetCode 2034 - Stock Price Fluctuation
// https://leetcode.com/problems/stock-price-fluctuation/

export class StockPrice {
    constructor() {
        this.latestTs = 0;
        this.priceAt = new Map();
        this.maxHeap = [];
        this.minHeap = [];
    }

    _pushMax(item: any): any {
        this.maxHeap.push(item);
        this.maxHeap.sort((a, b) => b[0] - a[0]);
    }
    _pushMin(item: any): any {
        this.minHeap.push(item);
        this.minHeap.sort((a, b) => a[0] - b[0]);
    }

    update(timestamp: any, price: any): any {
        this.priceAt.set(timestamp, price);
        if (timestamp >= this.latestTs) this.latestTs = timestamp;
        this._pushMax([price, timestamp]);
        this._pushMin([price, timestamp]);
    }

    current(): any {
        return this.priceAt.get(this.latestTs);
    }

    maximum(): any {
        while (true) {
            const top = this.maxHeap[0];
            if (this.priceAt.get(top[1]) === top[0]) return top[0];
            this.maxHeap.shift();
        }
    }

    minimum(): any {
        while (true) {
            const top = this.minHeap[0];
            if (this.priceAt.get(top[1]) === top[0]) return top[0];
            this.minHeap.shift();
        }
    }
}
