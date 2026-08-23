// LeetCode 2413 - Smallest Even Multiple
// https://leetcode.com/problems/smallest-even-multiple/

public class Solution {
    public int SmallestEvenMultiple(int n) {
        return n % 2 == 0 ? n : n * 2;
    }
}
