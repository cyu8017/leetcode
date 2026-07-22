// LeetCode 1618 - Maximum Font to Fit a Sentence in a Screen
// https://leetcode.com/problems/maximum-font-to-fit-a-sentence-in-a-screen/

public interface FontInfo {
    int GetWidth(int fontSize, char ch);
    int GetHeight(int fontSize);
}

public class DefaultFontInfo : FontInfo {
    public int GetWidth(int fontSize, char ch) => fontSize;
    public int GetHeight(int fontSize) => fontSize;
}

public class Solution {
    public int MaxFont(string text, int w, int h, int[] fonts, FontInfo fontInfo = null) {
        fontInfo ??= new DefaultFontInfo();
        int lo = 0, hi = fonts.Length - 1, ans = -1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            int f = fonts[mid];
            bool fits = fontInfo.GetHeight(f) <= h;
            if (fits) {
                long width = 0;
                foreach (char c in text) width += fontInfo.GetWidth(f, c);
                fits = width <= w;
            }
            if (fits) { ans = f; lo = mid + 1; }
            else hi = mid - 1;
        }
        return ans;
    }
}
