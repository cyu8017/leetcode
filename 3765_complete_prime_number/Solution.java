// LeetCode 3765 - Complete Prime Number
// https://leetcode.com/problems/complete_prime_number/

class Solution {
    private boolean isPrime(int x) {
        if (x < 2) return false;
        for (int i = 2; i * i <= x; i++) if (x % i == 0) return false;
        return true;
    }

    public boolean completePrime(int num) {
        String s = Integer.toString(num);
        int x = 0;
        for (char c : s.toCharArray()) {
            x = x * 10 + (c - '0');
            if (!isPrime(x)) return false;
        }
        x = 0;
        int p = 1;
        for (int i = s.length() - 1; i >= 0; i--) {
            x = p * (s.charAt(i) - '0') + x;
            p *= 10;
            if (!isPrime(x)) return false;
        }
        return true;
    }
}
