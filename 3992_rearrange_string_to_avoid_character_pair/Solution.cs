// LeetCode 3992 - Rearrange String to Avoid Character Pair
// https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/

public class Solution {
    public string RearrangeString(string s, char x, char y) {
        char[] arr = s.ToCharArray();
        int i = 0;
        for (int j = 0; j < arr.Length; j++) {
            if (arr[j] == y) {
                char tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
                i++;
            }
        }
        return new string(arr);
    }
}
