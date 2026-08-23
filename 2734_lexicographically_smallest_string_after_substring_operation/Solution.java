// LeetCode 2734 - Lexicographically Smallest String After Substring Operation
// https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/

class Solution {
    public String smallestString(String s) {
        char[] arr = s.toCharArray();
        int n = arr.length, i = 0;
        while (i < n && arr[i] == 'a') i++;
        if (i == n) { arr[n - 1] = 'z'; return new String(arr); }
        while (i < n && arr[i] != 'a') { arr[i]--; i++; }
        return new String(arr);
    }
}
