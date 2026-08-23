// LeetCode 0917 - Reverse Only Letters
// https://leetcode.com/problems/reverse-only-letters/

class Solution {
    public String reverseOnlyLetters(String s) {
        char[] arr = s.toCharArray();
        int i = 0, j = arr.length - 1;
        while (i < j) {
            while (i < j && !Character.isLetter(arr[i])) i++;
            while (i < j && !Character.isLetter(arr[j])) j--;
            char tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
            i++;
            j--;
        }
        return new String(arr);
    }
}
