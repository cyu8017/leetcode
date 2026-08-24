# LeetCode 3582 - Generate Tag for Video Caption
# https://leetcode.com/problems/generate-tag-for-video-caption/

# @param {String} caption
# @return {String}
def generate_tag(caption)
  ans = "#"
  words = caption.strip.split
  i = 0
  words.each do |word|
    next if word.empty?
    w = word.downcase
    if i == 0
      ans += w
    else
      w = w[0].upcase + w[1..] if w.length > 0
      ans += w
    end
    break if ans.length >= 100
    i += 1
  end
  ans = ans[0, 100] if ans.length > 100
  ans
end
