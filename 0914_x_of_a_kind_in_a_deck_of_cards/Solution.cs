// LeetCode 0914 - X of a Kind in a Deck of Cards
// https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/

using System.Collections.Generic;

public class Solution {
    public bool HasGroupsSizeX(int[] deck) {
        var count = new Dictionary<int, int>();
        foreach (int x in deck) {
            if (!count.ContainsKey(x)) count[x] = 0;
            count[x]++;
        }
        int g = 0;
        foreach (var c in count.Values) g = Gcd(g, c);
        return g >= 2;
    }
    private int Gcd(int a, int b) {
        while (b != 0) { int t = a % b; a = b; b = t; }
        return a;
    }
}
