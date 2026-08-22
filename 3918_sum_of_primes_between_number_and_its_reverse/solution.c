// LeetCode 3918 - Sum Of Primes Between Number And Its Reverse
// https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/

#include <stdbool.h>
#include <string.h>

static bool isPrime3918[1001];
static int ready3918 = 0;

static void init3918(void) {
    if (ready3918) return;
    memset(isPrime3918, 1, sizeof(isPrime3918));
    isPrime3918[0] = isPrime3918[1] = false;
    for (int i = 2; i * i <= 1000; i++) {
        if (isPrime3918[i])
            for (int j = i * i; j <= 1000; j += i) isPrime3918[j] = false;
    }
    ready3918 = 1;
}

int sumOfPrimesInRange(int n) {
    init3918();
    int r = 0;
    for (int x = n; x > 0; x /= 10) r = r * 10 + x % 10;
    int low = n < r ? n : r;
    int high = n > r ? n : r;
    int ans = 0;
    for (int x = low; x <= high; x++) if (isPrime3918[x]) ans += x;
    return ans;
}
