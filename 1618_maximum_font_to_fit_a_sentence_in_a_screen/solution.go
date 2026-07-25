// LeetCode 1618 - Maximum Font to Fit a Sentence in a Screen
// https://leetcode.com/problems/maximum-font-to-fit-a-sentence-in-a-screen/

type FontInfo interface {
	GetWidth(fontSize int, ch byte) int
	GetHeight(fontSize int) int
}

type defaultFontInfo struct{}

func (defaultFontInfo) GetWidth(fontSize int, ch byte) int { return fontSize }
func (defaultFontInfo) GetHeight(fontSize int) int         { return fontSize }

func maxFont(text string, w int, h int, fonts []int, fontInfo FontInfo) int {
	if fontInfo == nil {
		fontInfo = defaultFontInfo{}
	}
	lo, hi, ans := 0, len(fonts)-1, -1
	for lo <= hi {
		mid := (lo + hi) / 2
		f := fonts[mid]
		fits := fontInfo.GetHeight(f) <= h
		if fits {
			width := 0
			for i := 0; i < len(text); i++ {
				width += fontInfo.GetWidth(f, text[i])
			}
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
