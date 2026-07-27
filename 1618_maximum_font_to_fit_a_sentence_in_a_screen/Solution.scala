// LeetCode 1618 - Maximum Font to Fit a Sentence in a Screen
// https://leetcode.com/problems/maximum-font-to-fit-a-sentence-in-a-screen/

trait FontInfo {
  def getWidth(fontSize: Int, ch: Char): Int
  def getHeight(fontSize: Int): Int
}

object Solution {
  def maxFont(text: String, w: Int, h: Int, fonts: Array[Int], fontInfo: FontInfo): Int = {
    var lo = 0
    var hi = fonts.length - 1
    var ans = -1
    while (lo <= hi) {
      val mid = (lo + hi) / 2
      val f = fonts(mid)
      val heightOk = fontInfo.getHeight(f) <= h
      val widthOk = text.map(c => fontInfo.getWidth(f, c)).sum <= w
      if (heightOk && widthOk) {
        ans = f
        lo = mid + 1
      } else hi = mid - 1
    }
    ans
  }
}
