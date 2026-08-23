// LeetCode 0379 - Design Phone Directory
class PhoneDirectory {
    constructor(maxNumbers) {
        this.available = new Set(Array.from({ length: maxNumbers }, (_, index) => index));
    }

    get() {
        if (!this.available.size) return -1;
        const number = Math.min(...this.available);
        this.available.delete(number);
        return number;
    }

    check(number) {
        return this.available.has(number);
    }

    release(number) {
        this.available.add(number);
    }
}

module.exports = { PhoneDirectory };
