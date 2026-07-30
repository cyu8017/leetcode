// LeetCode 1227 - Airplane Seat Assignment Probability
// https://leetcode.com/problems/airplane-seat-assignment-probability/

public class Solution {
    public double NthPersonGetsNthSeat(int n) {
        return n == 1 ? 1.0 : 0.5;
    }
}
