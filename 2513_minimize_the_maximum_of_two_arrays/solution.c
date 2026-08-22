// LeetCode 2513 - Minimize the Maximum of Two Arrays
// https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

static int gcd2513(int a, int b) {
    while (b) { int t = a % b; a = b; b = t; }
    return a;
}

int minimizeSet(int divisor1, int divisor2, int uniqueCnt1, int uniqueCnt2) {
    long long lcm = (long long)divisor1 / gcd2513(divisor1, divisor2) * divisor2;
    long long lo = 1, hi = 1LL << 62;
    while (lo < hi) {
        long long mid = (lo + hi) / 2;
        long long a = mid - mid / divisor1;
        long long b = mid - mid / divisor2;
        long long both = mid - mid / lcm;
        if (a >= uniqueCnt1 && b >= uniqueCnt2 && both >= (long long)uniqueCnt1 + uniqueCnt2) hi = mid;
        else lo = mid + 1;
    }
    return (int)lo;
}
