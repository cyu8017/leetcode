# LeetCode 1943 - Describe the Painting
# https://leetcode.com/problems/describe-the-painting/

# @param {Integer[][]} segments
# @return {Integer[][]}
def split_painting(segments)
  diff = Hash.new(0)
  segments.each do |s, e, c|
    diff[s] += c
    diff[e] -= c
  end
  points = diff.keys.sort
  ans = []
  cur = 0
  (0...points.length - 1).each do |i|
    cur += diff[points[i]]
    ans << [points[i], points[i + 1], cur] if cur != 0
  end
  ans
end
