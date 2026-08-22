// LeetCode 3687 - Library Late Fee Calculator
// https://leetcode.com/problems/library-late-fee-calculator/

int lateFee(int* daysLate, int daysLateSize) {
    int ans = 0;
    for (int i = 0; i < daysLateSize; i++) {
        int x = daysLate[i];
        if (x == 1) ans += 1;
        else if (x > 5) ans += 3 * x;
        else ans += 2 * x;
    }
    return ans;
}
