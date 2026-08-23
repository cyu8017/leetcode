// LeetCode 2129 - Capitalize the Title
// https://leetcode.com/problems/capitalize-the-title/

class Solution {
    public String capitalizeTitle(String title) {
        String[] parts = title.trim().split("\\s+");
        for (int i = 0; i < parts.length; i++) {
            String w = parts[i].toLowerCase();
            if (w.length() > 2) w = Character.toUpperCase(w.charAt(0)) + w.substring(1);
            parts[i] = w;
        }
        return String.join(" ", parts);
    }
}
