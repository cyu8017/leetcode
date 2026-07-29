// LeetCode 1300 - Sum of Mutated Array Closest to Target
// https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

int findBestValue(int* arr, int arrSize, int target) {
    int hi = arr[0];
    for (int i = 1; i < arrSize; i++) if (arr[i] > hi) hi = arr[i];
    int lo = 0;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        long sum = 0;
        for (int i = 0; i < arrSize; i++) sum += arr[i] < mid ? arr[i] : mid;
        if (sum < target) lo = mid + 1;
        else hi = mid;
    }
    long before = 0, after = 0;
    for (int i = 0; i < arrSize; i++) {
        before += arr[i] < lo - 1 ? arr[i] : (lo - 1);
        after += arr[i] < lo ? arr[i] : lo;
    }
    return (target - before <= after - target) ? lo - 1 : lo;
}
