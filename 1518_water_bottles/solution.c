// LeetCode 1518 - Water Bottles
// https://leetcode.com/problems/water-bottles/

int numWaterBottles(int numBottles, int numExchange) {
    int total = numBottles;
    while (numBottles >= numExchange) {
        int neu = numBottles / numExchange;
        int rem = numBottles % numExchange;
        total += neu;
        numBottles = neu + rem;
    }
    return total;
}
