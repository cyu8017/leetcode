// LeetCode 0800 - Similar RGB Color
// https://leetcode.com/problems/similar-rgb-color/

class Solution {
    public String similarRGB(String color) {
        return "#" + closest(color.substring(1, 3)) + closest(color.substring(3, 5))
            + closest(color.substring(5, 7));
    }

    private String closest(String component) {
        int value = Integer.parseInt(component, 16);
        int rounded = (value + 8) / 17;
        return String.format("%x%x", rounded, rounded);
    }
}
