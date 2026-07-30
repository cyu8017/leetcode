// LeetCode 1518 - Water Bottles
// https://leetcode.com/problems/water-bottles/

public class Solution {
    public int NumWaterBottles(int numBottles, int numExchange) {
        int total = numBottles;
        while (numBottles >= numExchange) {
            int neu = numBottles / numExchange;
            int remainder = numBottles % numExchange;
            total += neu;
            numBottles = neu + remainder;
        }
        return total;
    }
}
