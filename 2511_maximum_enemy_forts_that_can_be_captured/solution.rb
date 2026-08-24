# LeetCode 2511 - Maximum Enemy Forts That Can Be Captured
# https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

# @param {Integer[]} forts
# @return {Integer}
def capture_forts(forts)
  ans = 0
  prev = -1
  forts.each_with_index do |f, i|
    next if f == 0

    ans = i - prev - 1 if prev >= 0 && forts[prev] == -f && i - prev - 1 > ans
    prev = i
  end
  ans
end
