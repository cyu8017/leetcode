// LeetCode 1114 - Print in Order
// https://leetcode.com/problems/print-in-order/

class Foo {
    p2: any;
    r2: any;
    p3: any;
    r3: any;

    constructor() {
        this.p2 = new Promise((resolve) => { this.r2 = resolve; });
        this.p3 = new Promise((resolve) => { this.r3 = resolve; });
    }

    async first(printFirst: any): Promise<void> {
        printFirst();
        this.r2();
    }

    async second(printSecond: any): Promise<void> {
        await this.p2;
        printSecond();
        this.r3();
    }

    async third(printThird: any): Promise<void> {
        await this.p3;
        printThird();
    }
}
