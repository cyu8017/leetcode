// LeetCode 3896 - Minimum Operations To Transform Array Into Alternating Prime
// https://leetcode.com/problems/minimum-operations-to-transform-array-into-alternating-prime/

using System.Collections.Generic;

public class Solution {
    const int MX = 200000;
    static bool[] isPrime;
    static List<int> primes;
    static bool ready = false;

    static void Init() {
        if (ready) return;
        isPrime = new bool[MX + 1];
        for (int i = 0; i <= MX; i++) isPrime[i] = true;
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i <= MX / i; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= MX; j += i) isPrime[j] = false;
            }
        }
        primes = new List<int>();
        for (int i = 2; i <= MX; i++) if (isPrime[i]) primes.Add(i);
        ready = true;
    }

    public int MinOperations(int[] nums) {
        Init();
        int ans = 0;
        for (int i = 0; i < nums.Length; i++) {
            int x = nums[i];
            if (i % 2 == 0) {
                int idx = primes.BinarySearch(x);
                if (idx < 0) idx = ~idx;
                ans += primes[idx] - x;
            } else if (isPrime[x]) {
                ans += (x == 2) ? 2 : 1;
            }
        }
        return ans;
    }
}
