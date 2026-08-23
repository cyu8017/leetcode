// LeetCode 3216 - Lexicographically Smallest String After a Swap
// https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/

public class Solution {
    public string GetSmallestString(string s) {
        char[] arr = s.ToCharArray();
        int n = arr.Length;
        for (int i = 1; i < n; i++) {
            char a = arr[i - 1], b = arr[i];
            if (a > b && (a % 2) == (b % 2)) {
                arr[i - 1] = b; arr[i] = a;
                return new string(arr);
            }
        }
        return s;
    }
}
