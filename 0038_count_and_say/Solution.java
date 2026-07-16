// LeetCode 0038 - Count and Say
// https://leetcode.com/problems/count-and-say/

class Solution {
    public String countAndSay(int n) {
        String term = "1";

        for (int i = 1; i < n; i++) {
            StringBuilder nextTerm = new StringBuilder();
            int index = 0;
            while (index < term.length()) {
                int count = 1;
                while (index + count < term.length() && term.charAt(index + count) == term.charAt(index)) {
                    count++;
                }
                nextTerm.append(count);
                nextTerm.append(term.charAt(index));
                index += count;
            }
            term = nextTerm.toString();
        }

        return term;
    }
}
