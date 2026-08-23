// LeetCode 3100 - Water Bottles II
// https://leetcode.com/problems/water-bottles-ii/

class Solution {
public:
    int maxBottlesDrunk(int numBottles, int numExchange) {
        int ans = numBottles;
        while (numBottles >= numExchange) {
            numBottles -= numExchange;
            numExchange++;
            ans++;
            numBottles++;
        }
        return ans;
    }
};
