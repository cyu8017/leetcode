export class HitCounter {
    private hits: number[];

    constructor() {
        this.hits = [];
    }

    hit(timestamp: number): void {
        this.hits.push(timestamp);
    }

    getHits(timestamp: number): number {
        while (this.hits.length && this.hits[0] <= timestamp - 300) {
            this.hits.shift();
        }
        return this.hits.length;
    }
}
