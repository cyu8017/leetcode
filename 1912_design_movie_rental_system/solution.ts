// LeetCode 1912 - Design Movie Rental System
// https://leetcode.com/problems/design-movie-rental-system/

class MovieRentingSystem {
    price: Map<string, number>;
    available: Map<number, number[][]>;
    rented: number[][];

    constructor(_n: number, entries: number[][]) {
        this.price = new Map();
        this.available = new Map();
        this.rented = [];
        for (const [shop, movie, price] of entries) {
            this.price.set(`${shop},${movie}`, price);
            if (!this.available.has(movie)) this.available.set(movie, []);
            this._insort(this.available.get(movie)!, [price, shop], (a: any, b: any) => a[0] - b[0] || a[1] - b[1]);
        }
    }

    _insort(arr: any[], item: any, cmp: (a: any, b: any) => number): void {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (cmp(arr[mid], item) < 0) lo = mid + 1;
            else hi = mid;
        }
        arr.splice(lo, 0, item);
    }

    _remove(arr: any[], item: any, eq: (a: any, b: any) => boolean): void {
        const i = arr.findIndex((x: any) => eq(x, item));
        if (i >= 0) arr.splice(i, 1);
    }

    search(movie: number): number[] {
        return (this.available.get(movie) || []).slice(0, 5).map((x: any) => x[1]);
    }

    rent(shop: number, movie: number): void {
        const price = this.price.get(`${shop},${movie}`)!;
        this._remove(this.available.get(movie)!, [price, shop], (a: any, b: any) => a[0] === b[0] && a[1] === b[1]);
        this._insort(this.rented, [price, shop, movie], (a: any, b: any) => a[0] - b[0] || a[1] - b[1] || a[2] - b[2]);
    }

    drop(shop: number, movie: number): void {
        const price = this.price.get(`${shop},${movie}`)!;
        this._remove(this.rented, [price, shop, movie], (a: any, b: any) => a[0] === b[0] && a[1] === b[1] && a[2] === b[2]);
        this._insort(this.available.get(movie)!, [price, shop], (a: any, b: any) => a[0] - b[0] || a[1] - b[1]);
    }

    report(): number[][] {
        return this.rented.slice(0, 5).map((x: any) => [x[1], x[2]]);
    }
}
