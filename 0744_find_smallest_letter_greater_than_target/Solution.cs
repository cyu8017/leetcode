// LeetCode 0744 - Find Smallest Letter Greater Than Target
// https://leetcode.com/problems/find-smallest-letter-greater-than-target/

public class Solution {
    public char NextGreatestLetter(char[] letters, char target) {
        int left = 0, right = letters.Length;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (letters[mid] <= target) left = mid + 1;
            else right = mid;
        }
        return letters[left % letters.Length];
    }
}
