// LeetCode 0848 - Shifting Letters
// https://leetcode.com/problems/shifting-letters/

class Solution {
    public String shiftingLetters(String s, int[] shifts) {
        char[] arr = s.toCharArray();
        int total = 0;
        for (int i = arr.length - 1; i >= 0; i--) {
            total = (total + shifts[i]) % 26;
            arr[i] = (char) ((arr[i] - 'a' + total) % 26 + 'a');
        }
        return new String(arr);
    }
}
