// LeetCode 3582 - Generate Tag for Video Caption
// https://leetcode.com/problems/generate-tag-for-video-caption/

class Solution {
    public String generateTag(String caption) {
        StringBuilder ans = new StringBuilder("#");
        String[] words = caption.trim().split("\\s+");
        int i = 0;
        for (String word : words) {
            if (word.isEmpty()) continue;
            StringBuilder w = new StringBuilder(word.toLowerCase());
            if (i == 0) ans.append(w);
            else {
                if (w.length() > 0) w.setCharAt(0, Character.toUpperCase(w.charAt(0)));
                ans.append(w);
            }
            if (ans.length() >= 100) break;
            i++;
        }
        if (ans.length() > 100) ans.setLength(100);
        return ans.toString();
    }
}
