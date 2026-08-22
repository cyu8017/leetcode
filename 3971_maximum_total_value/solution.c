// LeetCode 3971 - Maximum Total Value
// https://leetcode.com/problems/maximum-total-value/

enum { MOD3971 = 1000000007LL };

static long long countAtLeast3971(int* value, int* decay, int n, long long threshold) {
    long long count = 0;
    for (int i = 0; i < n; i++) {
        if (value[i] >= threshold)
            count += (value[i] - threshold) / decay[i] + 1;
    }
    return count;
}

int maximumTotalValue(int* value, int valueSize, int* decay, int decaySize, long long m) {
    (void)decaySize;
    int n = valueSize;
    if (countAtLeast3971(value, decay, n, 1) <= m) {
        long long sum = 0;
        for (int i = 0; i < n; i++) {
            long long terms = (value[i] - 1LL) / decay[i] + 1;
            sum = (sum + terms * value[i] - (long long)decay[i] * terms * (terms - 1) / 2) % MOD3971;
        }
        return (int)sum;
    }
    long long high = 0;
    for (int i = 0; i < n; i++) if (value[i] > high) high = value[i];
    long long low = 1;
    while (low < high) {
        long long mid = (low + high + 1) / 2;
        if (countAtLeast3971(value, decay, n, mid) >= m) low = mid;
        else high = mid - 1;
    }
    long long threshold = low;
    long long count = 0, sum = 0;
    for (int i = 0; i < n; i++) {
        if (value[i] < threshold) continue;
        long long terms = (value[i] - threshold) / decay[i] + 1;
        count += terms;
        sum = (sum + (terms * value[i] - (long long)decay[i] * terms * (terms - 1) / 2) % MOD3971) % MOD3971;
    }
    sum = (sum - ((count - m) % MOD3971) * (threshold % MOD3971)) % MOD3971;
    if (sum < 0) sum += MOD3971;
    return (int)sum;
}
