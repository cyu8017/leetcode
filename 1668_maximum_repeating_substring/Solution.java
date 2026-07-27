// LeetCode 1668 - Maximum Repeating Substring
// https://leetcode.com/problems/maximum-repeating-substring/

class Solution {
    public int maxRepeating(String sequence, String word) {
        int k = 0;
        StringBuilder sb = new StringBuilder();
        while (true) {
            sb.append(word);
            if (!sequence.contains(sb.toString())) {
                break;
            }
            k++;
        }
        return k;
    }
}
