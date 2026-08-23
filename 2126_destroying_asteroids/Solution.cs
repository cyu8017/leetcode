// LeetCode 2126 - Destroying Asteroids
// https://leetcode.com/problems/destroying-asteroids/

public class Solution {
    public bool AsteroidsDestroyed(int mass, int[] asteroids) {
        Array.Sort(asteroids);
        long cur = mass;
        foreach (int a in asteroids) {
            if (cur < a) return false;
            cur += a;
        }
        return true;
    }
}
