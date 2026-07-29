// LeetCode 1599 - Maximum Profit of Operating a Centennial Wheel
// https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/

int minOperationsMaxProfit(int* customers, int customersSize, int boardingCost, int runningCost) {
    int waiting = 0, profit = 0, best = 0, answer = 0, rotation = 0, i = 0;
    while (i < customersSize || waiting) {
        if (i < customersSize) waiting += customers[i];
        int boarded = waiting < 4 ? waiting : 4;
        waiting -= boarded;
        rotation++;
        profit += boarded * boardingCost - runningCost;
        if (profit > best) {
            best = profit;
            answer = rotation;
        }
        i++;
    }
    return best > 0 ? answer : -1;
}
