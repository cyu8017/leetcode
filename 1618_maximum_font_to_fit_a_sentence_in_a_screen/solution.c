// LeetCode 1618 - Maximum Font to Fit a Sentence in a Screen
// https://leetcode.com/problems/maximum-font-to-fit-a-sentence-in-a-screen/

#include <stdbool.h>

/**
 * // This is the FontInfo's API interface.
 * // You should not implement it, or speculate about its implementation
 */
struct FontInfo {
    int (*getWidth)(struct FontInfo*, int fontSize, char ch);
    int (*getHeight)(struct FontInfo*, int fontSize);
};

static bool fits(char* text, int w, int h, int f, struct FontInfo* fontInfo) {
    if (fontInfo->getHeight(fontInfo, f) > h) return false;
    long long width = 0;
    for (char* p = text; *p; p++) width += fontInfo->getWidth(fontInfo, f, *p);
    return width <= w;
}

int maxFont(char* text, int w, int h, int* fonts, int fontsSize, struct FontInfo* fontInfo) {
    int lo = 0, hi = fontsSize - 1, ans = -1;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        if (fits(text, w, h, fonts[mid], fontInfo)) {
            ans = fonts[mid];
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    return ans;
}
