// LeetCode 0440 - K-th Smallest in Lexicographical Order
// https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

static int countSteps(int n, long long first, long long last) {
    int steps = 0;
    while (first <= n) {
        long long upper = last < (long long)n + 1 ? last : (long long)n + 1;
        steps += (int)(upper - first);
        first *= 10;
        last *= 10;
    }
    return steps;
}

int findKthNumber(int n, int k) {
    int current = 1;
    k -= 1;
    while (k > 0) {
        int steps = countSteps(n, current, (long long)current + 1);
        if (steps <= k) {
            current += 1;
            k -= steps;
        } else {
            current *= 10;
            k -= 1;
        }
    }
    return current;
}
