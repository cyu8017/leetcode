// LeetCode 3918 - Sum Of Primes Between Number And Its Reverse
// https://leetcode.com/problems/sum-of-primes-between-number-and-its-reverse/

class Solution {
    static boolean ready = false;
    static boolean[] isPrime;

    static void Init() {
        if (ready) return;
        isPrime = new boolean[1001];
        for (int i = 0; i <= 1000; i++) isPrime[i] = true;
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i <= 1000; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= 1000; j += i) isPrime[j] = false;
            }
        }
        ready = true;
    }

    public int sumOfPrimesInRange(int n) {
        Init();
        int r = 0;
        for (int x = n; x > 0; x /= 10) r = r * 10 + x % 10;
        int low = Math.min(n, r), high = Math.max(n, r);
        int ans = 0;
        for (int x = low; x <= high; x++) {
            if (isPrime[x]) ans += x;
        }
        return ans;
    }
}
