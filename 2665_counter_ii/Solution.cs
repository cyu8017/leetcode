// LeetCode 2665 - Counter II
// https://leetcode.com/problems/counter-ii/

// JS Counter II stand-in
public class CounterII {
    int init_, cur_;
    public CounterII(int init) { init_ = cur_ = init; }
    public int Increment() => ++cur_;
    public int Decrement() => --cur_;
    public int Reset() { cur_ = init_; return cur_; }
}

public class Solution {
    public CounterII CreateCounter(int init) {
        return new CounterII(init);
    }
}
