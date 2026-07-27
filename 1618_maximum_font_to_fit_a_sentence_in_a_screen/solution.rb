# LeetCode 1618 - Maximum Font to Fit a Sentence in a Screen
# https://leetcode.com/problems/maximum-font-to-fit-a-sentence-in-a-screen/

class FontInfo
  def get_width(font_size, _ch)
    font_size
  end

  def get_height(font_size)
    font_size
  end

  alias getWidth get_width
  alias getHeight get_height
end

# @param {String} text
# @param {Integer} w
# @param {Integer} h
# @param {Integer[]} fonts
# @param {FontInfo} font_info
# @return {Integer}
def max_font(text, w, h, fonts, font_info = nil)
  font_info ||= FontInfo.new
  lo = 0
  hi = fonts.length - 1
  ans = -1
  while lo <= hi
    mid = (lo + hi) / 2
    f = fonts[mid]
    height = font_info.respond_to?(:getHeight) ? font_info.getHeight(f) : font_info.get_height(f)
    width = text.chars.sum do |c|
      font_info.respond_to?(:getWidth) ? font_info.getWidth(f, c) : font_info.get_width(f, c)
    end
    if height <= h && width <= w
      ans = f
      lo = mid + 1
    else
      hi = mid - 1
    end
  end
  ans
end
