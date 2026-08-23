// LeetCode 0660 - Remove 9
// https://leetcode.com/problems/remove-9/

public class Solution {
    public int NewInteger(int n) {
        int result = 0, bas = 1;
        while (n > 0) {
            result += (n % 9) * bas;
            n /= 9;
            bas *= 10;
        }
        return result;
    }
}
