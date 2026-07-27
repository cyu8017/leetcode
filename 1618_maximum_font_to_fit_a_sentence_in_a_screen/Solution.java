// LeetCode 1618 - Maximum Font to Fit a Sentence in a Screen
// https://leetcode.com/problems/maximum-font-to-fit-a-sentence-in-a-screen/

interface FontInfo {
    int getWidth(int fontSize, char ch);
    int getHeight(int fontSize);
}

class Solution {
    public int maxFont(String text, int w, int h, int[] fonts, FontInfo fontInfo) {
        int lo = 0, hi = fonts.length - 1, ans = -1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            int f = fonts[mid];
            boolean fits = fontInfo.getHeight(f) <= h;
            if (fits) {
                long width = 0;
                for (char c : text.toCharArray()) width += fontInfo.getWidth(f, c);
                fits = width <= w;
            }
            if (fits) {
                ans = f;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return ans;
    }

    public int maxFont(String text, int w, int h, int[] fonts) {
        return maxFont(text, w, h, fonts, new FontInfo() {
            public int getWidth(int fontSize, char ch) { return fontSize; }
            public int getHeight(int fontSize) { return fontSize; }
        });
    }
}
