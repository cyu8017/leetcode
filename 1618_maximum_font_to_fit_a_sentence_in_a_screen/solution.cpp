// LeetCode 1618 - Maximum Font to Fit a Sentence in a Screen
// https://leetcode.com/problems/maximum-font-to-fit-a-sentence-in-a-screen/

#include <string>
#include <vector>

// Stub FontInfo matching the problem's test harness defaults.
class FontInfo {
public:
    virtual int getWidth(int fontSize, char ch) {
        (void)ch;
        return fontSize;
    }
    virtual int getHeight(int fontSize) { return fontSize; }
    virtual ~FontInfo() = default;
};

class Solution {
public:
    int maxFont(std::string text, int w, int h, std::vector<int>& fonts, FontInfo* fontInfo = nullptr) {
        FontInfo defaultInfo;
        if (!fontInfo) {
            fontInfo = &defaultInfo;
        }
        int lo = 0, hi = static_cast<int>(fonts.size()) - 1, ans = -1;
        while (lo <= hi) {
            const int mid = (lo + hi) / 2;
            const int f = fonts[mid];
            bool fits = fontInfo->getHeight(f) <= h;
            if (fits) {
                long long width = 0;
                for (char c : text) {
                    width += fontInfo->getWidth(f, c);
                }
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
};
