// LeetCode 3577 - Count the Number of Computer Unlocking Permutations
// https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

public class Solution {
    public int CountPermutations(int[] complexity) {
        const long mod = 1000000007;
        long ans = 1;
        for (int i = 1; i < complexity.Length; i++) {
            if (complexity[i] <= complexity[0]) return 0;
            ans = ans * i % mod;
        }
        return (int)ans;
    }
}
