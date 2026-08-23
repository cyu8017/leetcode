// LeetCode 3992 - Rearrange String to Avoid Character Pair
// https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/

class Solution {
    public String rearrangeString(String s, char x, char y) {
        char[] arr = s.toCharArray();
        int i = 0;
        for (int j = 0; j < arr.length; j++) {
            if (arr[j] == y) {
                char tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
                i++;
            }
        }
        return new String(arr);
    }
}
