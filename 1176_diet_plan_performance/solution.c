// LeetCode 1176 - Diet Plan Performance
// https://leetcode.com/problems/diet-plan-performance/

int dietPlanPerformance(int* calories, int caloriesSize, int k, int lower, int upper) {
    int window = 0;
    for (int i = 0; i < k; i++) window += calories[i];
    int ans = 0;
    if (window < lower) ans--;
    else if (window > upper) ans++;
    for (int i = k; i < caloriesSize; i++) {
        window += calories[i] - calories[i - k];
        if (window < lower) ans--;
        else if (window > upper) ans++;
    }
    return ans;
}
