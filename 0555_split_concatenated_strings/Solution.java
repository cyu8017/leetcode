// LeetCode 0555 - Split Concatenated Strings
// https://leetcode.com/problems/split-concatenated-strings/

class Solution {
    public String splitLoopedString(String[] strs) {
        String[] bestForms = new String[strs.length];
        for (int i = 0; i < strs.length; ++i) {
            String s = strs[i];
            String rev = new StringBuilder(s).reverse().toString();
            bestForms[i] = s.compareTo(rev) >= 0 ? s : rev;
        }

        String answer = "";
        for (int i = 0; i < strs.length; ++i) {
            StringBuilder midBuilder = new StringBuilder();
            for (int j = i + 1; j < strs.length; ++j) {
                midBuilder.append(bestForms[j]);
            }
            for (int j = 0; j < i; ++j) {
                midBuilder.append(bestForms[j]);
            }
            String mid = midBuilder.toString();

            String original = strs[i];
            String reversed = new StringBuilder(original).reverse().toString();
            String[] candidates = {original, reversed};

            for (String candidate : candidates) {
                for (int cut = 0; cut < candidate.length(); ++cut) {
                    String formed = candidate.substring(cut) + mid + candidate.substring(0, cut);
                    if (formed.compareTo(answer) > 0) {
                        answer = formed;
                    }
                }
            }
        }
        return answer;
    }
}
