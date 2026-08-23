// LeetCode 2704 - To Be Or Not To Be
// https://leetcode.com/problems/to-be-or-not-to-be/

class Expect {
    private final int val;

    public Expect(int v) {
        val = v;
    }

    public boolean toBe(int other) {
        if (val == other) return true;
        throw new RuntimeException("Not Equal");
    }

    public boolean notToBe(int other) {
        if (val != other) return true;
        throw new RuntimeException("Equal");
    }
}

class Solution {
    public Expect expect(int val) {
        return new Expect(val);
    }
}
