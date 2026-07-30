// LeetCode 1447 - Simplified Fractions
// https://leetcode.com/problems/simplified-fractions/

using System.Collections.Generic;
public class Solution {
    public IList<string> SimplifiedFractions(int n) {
        var answer = new List<string>();
        for (int a = 1; a < n; a++)
            for (int b = a + 1; b <= n; b++)
                if (Gcd(a, b) == 1) answer.Add($"{a}/{b}");
        return answer;
    }
    int Gcd(int a, int b) { while (b != 0) { int t = a % b; a = b; b = t; } return a; }
}
