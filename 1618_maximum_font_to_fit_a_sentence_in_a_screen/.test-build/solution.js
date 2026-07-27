"use strict";
// LeetCode 1618 - Maximum Font to Fit a Sentence in a Screen
// https://leetcode.com/problems/maximum-font-to-fit-a-sentence-in-a-screen/
function maxFont(text, w, h, fonts, fontInfo = null) {
    const info = fontInfo || {
        getWidth: (fontSize, _ch) => fontSize,
        getHeight: (fontSize) => fontSize,
    };
    let lo = 0, hi = fonts.length - 1, ans = -1;
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        const f = fonts[mid];
        let width = 0;
        for (const c of text)
            width += info.getWidth(f, c);
        const fits = info.getHeight(f) <= h && width <= w;
        if (fits) {
            ans = f;
            lo = mid + 1;
        }
        else
            hi = mid - 1;
    }
    return ans;
}
