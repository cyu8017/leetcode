// LeetCode 1952 - Three Divisors
// https://leetcode.com/problems/three-divisors/

public class Solution {
    public bool IsThree(int n) {
        int root = (int)System.Math.Sqrt(n);
        if (root * root != n || root < 2) return false;
        for (int i = 2; i * i <= root; i++)
            if (root % i == 0) return false;
        return true;
    }
}