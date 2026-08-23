// LeetCode 0800 - Similar RGB Color
// https://leetcode.com/problems/similar-rgb-color/

using System;

public class Solution {
    public string SimilarRGB(string color) {
        string Closest(string component) {
            int value = Convert.ToInt32(component, 16);
            int rounded = (value + 8) / 17;
            return $"{rounded:x}{rounded:x}";
        }
        return "#" + Closest(color.Substring(1, 2)) + Closest(color.Substring(3, 2)) + Closest(color.Substring(5, 2));
    }
}
