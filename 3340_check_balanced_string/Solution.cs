// LeetCode 3340 - Check Balanced String
// https://leetcode.com/problems/check-balanced-string/

public class Solution {
    public bool IsBalanced(string num) {
        int even = 0, odd = 0;
        for (int i = 0; i < num.Length; i++) {
            if (i % 2 == 0) even += num[i] - '0';
            else odd += num[i] - '0';
        }
        return even == odd;
    }
}
