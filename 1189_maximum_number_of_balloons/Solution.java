// LeetCode 1189 - Maximum Number of Balloons
// https://leetcode.com/problems/maximum-number-of-balloons/

class Solution {
    public int maxNumberOfBalloons(String text) {
        int[] count = new int[26];
        for (char c : text.toCharArray()) count[c - 'a']++;
        return Math.min(Math.min(count[1], count[0]),
            Math.min(Math.min(count[11] / 2, count[14] / 2), count[13]));
    }
}
