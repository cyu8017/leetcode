// LeetCode 1011 - Capacity To Ship Packages Within D Days
// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

static int can_ship(int* weights, int n, int days, int cap) {
    int need = 1, cur = 0;
    for (int i = 0; i < n; i++) {
        if (cur + weights[i] > cap) {
            need++;
            cur = 0;
        }
        cur += weights[i];
    }
    return need <= days;
}

int shipWithinDays(int* weights, int weightsSize, int days) {
    int lo = 0, hi = 0;
    for (int i = 0; i < weightsSize; i++) {
        if (weights[i] > lo) lo = weights[i];
        hi += weights[i];
    }
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (can_ship(weights, weightsSize, days, mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
