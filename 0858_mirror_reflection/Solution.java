// LeetCode 0858 - Mirror Reflection
// https://leetcode.com/problems/mirror-reflection/

class Solution {
    public int mirrorReflection(int p, int q) {
        int g = gcd(p, q);
        p /= g;
        q /= g;
        if (p % 2 == 0) return 2;
        if (q % 2 == 0) return 0;
        return 1;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}
