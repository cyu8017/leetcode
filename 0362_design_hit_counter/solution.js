// LeetCode 0362 - Design Hit Counter
class HitCounter {
    constructor() {
        this.hits = [];
    }

    hit(timestamp) {
        this.hits.push(timestamp);
    }

    getHits(timestamp) {
        while (this.hits.length && this.hits[0] <= timestamp - 300) {
            this.hits.shift();
        }
        return this.hits.length;
    }
}

module.exports = { HitCounter };
