# LeetCode 3208 - Alternating Groups II
# https://leetcode.com/problems/alternating-groups-ii/

# @param {Integer[]} colors
# @param {Integer} k
# @return {Integer}
def number_of_alternating_groups(colors, k)
  n = colors.length
  cnt = 0
  ans = 0
  (0...(n * 2)).each do |i|
    if i > 0 && colors[i % n] == colors[(i - 1) % n]
      cnt = 1
    else
      cnt += 1
    end
    ans += 1 if i >= n && cnt >= k
  end
  ans
end
