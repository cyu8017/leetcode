// LeetCode 2734 - Lexicographically Smallest String After Substring Operation
// https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/

public class Solution {
    public string SmallestString(string s) {
        char[] arr = s.ToCharArray();
        int n = arr.Length, i = 0;
        while (i < n && arr[i] == 'a') i++;
        if (i == n) { arr[n - 1] = 'z'; return new string(arr); }
        while (i < n && arr[i] != 'a') { arr[i]--; i++; }
        return new string(arr);
    }
}
