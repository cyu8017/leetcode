// LeetCode 0858 - Mirror Reflection
// https://leetcode.com/problems/mirror-reflection/

using System;

public class Solution {
    public int MirrorReflection(int p, int q) {
        int g = Gcd(p, q);
        p /= g;
        q /= g;
        if (p % 2 == 0) return 2;
        if (q % 2 == 0) return 0;
        return 1;
    }

    private static int Gcd(int a, int b) {
        while (b != 0) { int t = a % b; a = b; b = t; }
        return a;
    }
}
