// LeetCode 3216 - Lexicographically Smallest String After a Swap
// https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/

class Solution {
    public String getSmallestString(String s) {
        char[] arr = s.toCharArray();
        int n = arr.length;
        for (int i = 1; i < n; i++) {
            char a = arr[i - 1], b = arr[i];
            if (a > b && (a % 2) == (b % 2)) {
                arr[i - 1] = b; arr[i] = a;
                return new String(arr);
            }
        }
        return s;
    }
}
