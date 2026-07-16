export class PhoneDirectory {
    private available: Set<number>;

    constructor(maxNumbers: number) {
        this.available = new Set(Array.from({ length: maxNumbers }, (_, index) => index));
    }

    get(): number {
        if (!this.available.size) return -1;
        const number = Math.min(...this.available);
        this.available.delete(number);
        return number;
    }

    check(number: number): boolean {
        return this.available.has(number);
    }

    release(number: number): void {
        this.available.add(number);
    }
}
