// LeetCode 1114 - Print in Order
// https://leetcode.com/problems/print-in-order/

var Foo = function() {
    this.p2 = new Promise((resolve) => { this.r2 = resolve; });
    this.p3 = new Promise((resolve) => { this.r3 = resolve; });
};

Foo.prototype.first = async function(printFirst) {
    printFirst();
    this.r2();
};

Foo.prototype.second = async function(printSecond) {
    await this.p2;
    printSecond();
    this.r3();
};

Foo.prototype.third = async function(printThird) {
    await this.p3;
    printThird();
};
