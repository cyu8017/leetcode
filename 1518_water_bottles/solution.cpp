// LeetCode 1518 - Water Bottles
// https://leetcode.com/problems/water-bottles/

class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int total = numBottles;
        while (numBottles >= numExchange) {
            const int exchanged = numBottles / numExchange;
            const int remainder = numBottles % numExchange;
            total += exchanged;
            numBottles = exchanged + remainder;
        }
        return total;
    }
};
