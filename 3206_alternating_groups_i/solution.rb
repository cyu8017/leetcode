# LeetCode 3206 - Alternating Groups I
# https://leetcode.com/problems/alternating-groups-i/

# @param {Integer[]} colors
# @return {Integer}
def number_of_alternating_groups(colors)
  k = 3
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
