// LeetCode 1912 - Design Movie Rental System
// https://leetcode.com/problems/design-movie-rental-system/

class MovieRentingSystem {
    /**
     * @param {number} n
     * @param {number[][]} entries
     */
    constructor(n, entries) {
        this.price = new Map();
        this.available = new Map();
        this.rented = [];
        for (const [shop, movie, price] of entries) {
            this.price.set(`${shop},${movie}`, price);
            if (!this.available.has(movie)) this.available.set(movie, []);
            this._insort(this.available.get(movie), [price, shop], (a, b) => a[0] - b[0] || a[1] - b[1]);
        }
    }

    _insort(arr, item, cmp) {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (cmp(arr[mid], item) < 0) lo = mid + 1;
            else hi = mid;
        }
        arr.splice(lo, 0, item);
    }

    _remove(arr, item, eq) {
        const i = arr.findIndex((x) => eq(x, item));
        if (i >= 0) arr.splice(i, 1);
    }

    /**
     * @param {number} movie
     * @return {number[]}
     */
    search(movie) {
        return (this.available.get(movie) || []).slice(0, 5).map((x) => x[1]);
    }

    /**
     * @param {number} shop
     * @param {number} movie
     * @return {void}
     */
    rent(shop, movie) {
        const price = this.price.get(`${shop},${movie}`);
        this._remove(this.available.get(movie), [price, shop], (a, b) => a[0] === b[0] && a[1] === b[1]);
        this._insort(this.rented, [price, shop, movie], (a, b) => a[0] - b[0] || a[1] - b[1] || a[2] - b[2]);
    }

    /**
     * @param {number} shop
     * @param {number} movie
     * @return {void}
     */
    drop(shop, movie) {
        const price = this.price.get(`${shop},${movie}`);
        this._remove(this.rented, [price, shop, movie], (a, b) => a[0] === b[0] && a[1] === b[1] && a[2] === b[2]);
        this._insort(this.available.get(movie), [price, shop], (a, b) => a[0] - b[0] || a[1] - b[1]);
    }

    /**
     * @return {number[][]}
     */
    report() {
        return this.rented.slice(0, 5).map((x) => [x[1], x[2]]);
    }
}
