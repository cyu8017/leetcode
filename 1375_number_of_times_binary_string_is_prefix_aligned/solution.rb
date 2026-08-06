# LeetCode 1375 - Number Of Times Binary String Is Prefix Aligned
# https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

def num_times_all_blue(flips)
  ans = 0
  mx = 0
  flips.each_with_index do |x, i|
    mx = [mx, x].max
    ans += 1 if mx == i + 1
  end
  ans
end
