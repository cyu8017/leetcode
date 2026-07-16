// LeetCode 0202 - Happy Number
#include <stdbool.h>

static int nextValue(int n) { int total = 0; while (n) { int digit = n % 10; total += digit * digit; n /= 10; } return total; }
bool isHappy(int n) {
    bool seen[1000] = {false};
    while (n != 1) {
        n = nextValue(n);
        if (n == 1) return true;
        if (seen[n]) return false;
        seen[n] = true;
    }
    return true;
}
