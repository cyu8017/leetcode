// LeetCode 1529 - Minimum Suffix Flips
// https://leetcode.com/problems/minimum-suffix-flips/

class Solution {
    public int minFlips(String target) {
        int answer = 0;
        char previous = '0';
        for (int i = 0; i < target.length(); i++) {
            char current = target.charAt(i);
            if (current != previous) {
                answer++;
            }
            previous = current;
        }
        return answer;
    }
}
