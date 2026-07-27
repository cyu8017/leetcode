// LeetCode 1618 - Maximum Font to Fit a Sentence in a Screen
// https://leetcode.com/problems/maximum-font-to-fit-a-sentence-in-a-screen/

protocol FontInfo {
    func getWidth(_ fontSize: Int, _ ch: Character) -> Int
    func getHeight(_ fontSize: Int) -> Int
}

private struct DefaultFontInfo: FontInfo {
    func getWidth(_ fontSize: Int, _ ch: Character) -> Int { fontSize }
    func getHeight(_ fontSize: Int) -> Int { fontSize }
}

class Solution {
    func maxFont(_ text: String, _ w: Int, _ h: Int, _ fonts: [Int], _ fontInfo: FontInfo) -> Int {
        var lo = 0, hi = fonts.count - 1, ans = -1
        let chars = Array(text)
        while lo <= hi {
            let mid = (lo + hi) / 2
            let f = fonts[mid]
            var fits = fontInfo.getHeight(f) <= h
            if fits {
                var width = 0
                for ch in chars { width += fontInfo.getWidth(f, ch) }
                fits = width <= w
            }
            if fits {
                ans = f
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        return ans
    }

    func maxFont(_ text: String, _ w: Int, _ h: Int, _ fonts: [Int]) -> Int {
        maxFont(text, w, h, fonts, DefaultFontInfo())
    }
}
