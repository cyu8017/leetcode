// LeetCode 2627 - Debounce
// https://leetcode.com/problems/debounce/

// JavaScript problem; Java stand-in (immediate invoke; no timer runtime).
class Solution {
    public Runnable debounce(Runnable fn, int t) {
        return () -> fn.run();
    }
}
