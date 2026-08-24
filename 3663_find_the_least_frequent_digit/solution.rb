# LeetCode 3663 - Find The Least Frequent Digit
# https://leetcode.com/problems/find-the-least-frequent-digit/

# @param {Integer} n
# @return {Integer}
def get_least_frequent_digit(n)
  cnt = Array.new(10, 0)
  ans = 0
  f = 1 << 30
  while n > 0
    cnt[n % 10] += 1
    n /= 10
  end
  (0...10).each do |x|
    if cnt[x] > 0 && cnt[x] < f
      f = cnt[x]
      ans = x
    end
  end
  ans
end
