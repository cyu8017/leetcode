// LeetCode 1819 - Number of Different Subsequences GCDs
// https://leetcode.com/problems/number-of-different-subsequences-gcds/

class Solution {
    public int countDifferentSubsequenceGCDs(int[] nums) {
        int maxVal = 0;
        for (int num : nums) {
            maxVal = Math.max(maxVal, num);
        }

        boolean[] present = new boolean[maxVal + 1];
        for (int num : nums) {
            present[num] = true;
        }

        int ans = 0;
        for (int g = 1; g <= maxVal; g++) {
            boolean has = false;
            int gcdVal = 0;
            for (int multiple = g; multiple <= maxVal; multiple += g) {
                if (present[multiple]) {
                    has = true;
                    gcdVal = gcd(gcdVal, multiple / g);
                    if (gcdVal == 1) {
                        break;
                    }
                }
            }
            if (has && gcdVal == 1) {
                ans++;
            }
        }
        return ans;
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
}
