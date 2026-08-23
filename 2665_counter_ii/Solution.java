// LeetCode 2665 - Counter II
// https://leetcode.com/problems/counter-ii/

// JS Counter II stand-in
class CounterII {
    private final int init;
    private int cur;

    public CounterII(int init) {
        this.init = this.cur = init;
    }

    public int increment() {
        return ++cur;
    }

    public int decrement() {
        return --cur;
    }

    public int reset() {
        cur = init;
        return cur;
    }
}

class Solution {
    public CounterII createCounter(int init) {
        return new CounterII(init);
    }
}
