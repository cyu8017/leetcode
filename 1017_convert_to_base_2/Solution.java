// LeetCode 1017 - Convert to Base -2
// https://leetcode.com/problems/convert-to-base-2/

class Solution {
    public String baseNeg2(int n) {
        if (n == 0) return "0";
        StringBuilder ans = new StringBuilder();
        while (n != 0) {
            int rem = n % -2;
            n /= -2;
            if (rem < 0) {
                n++;
                rem += 2;
            }
            ans.append(rem);
        }
        return ans.reverse().toString();
    }
}
