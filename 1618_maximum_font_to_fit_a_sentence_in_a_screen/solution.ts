// LeetCode 1618 - Maximum Font to Fit a Sentence in a Screen
// https://leetcode.com/problems/maximum-font-to-fit-a-sentence-in-a-screen/

interface FontInfo {
    getWidth(fontSize: number, ch: string): number;
    getHeight(fontSize: number): number;
}

function maxFont(
    text: string,
    w: number,
    h: number,
    fonts: number[],
    fontInfo: FontInfo | null = null,
): number {
    const info: FontInfo = fontInfo || {
        getWidth: (fontSize: number, _ch: string) => fontSize,
        getHeight: (fontSize: number) => fontSize,
    };
    let lo = 0, hi = fonts.length - 1, ans = -1;
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        const f = fonts[mid];
        let width = 0;
        for (const c of text) width += info.getWidth(f, c);
        const fits = info.getHeight(f) <= h && width <= w;
        if (fits) {
            ans = f;
            lo = mid + 1;
        } else hi = mid - 1;
    }
    return ans;
}
