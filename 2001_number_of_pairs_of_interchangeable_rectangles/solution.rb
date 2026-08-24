# LeetCode 2001 - Number of Pairs of Interchangeable Rectangles
# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

# @param {Integer[][]} rectangles
# @return {Integer}
def interchangeable_rectangles(rectangles)
  gcd = lambda do |a, b|
    a, b = b, a % b while b != 0
    a
  end
  freq = {}
  ans = 0
  rectangles.each do |w, h|
    g = gcd.call(w, h)
    key = [w / g, h / g]
    f = freq[key] || 0
    ans += f
    freq[key] = f + 1
  end
  ans
end
