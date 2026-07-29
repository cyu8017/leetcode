// LeetCode 0858 - Mirror Reflection
// https://leetcode.com/problems/mirror-reflection/

static int gcd(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

int mirrorReflection(int p, int q) {
    int g = gcd(p, q);
    p /= g;
    q /= g;
    if (p % 2 == 0) return 2;
    if (q % 2 == 0) return 0;
    return 1;
}
