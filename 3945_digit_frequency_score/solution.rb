# LeetCode 3945 - Digit Frequency Score
# https://leetcode.com/problems/digit-frequency-score/

# @param {Integer} n
# @return {Integer}
def digit_frequency_score(n)
  ans = 0
  while n > 0
    ans += n % 10
    n /= 10
  end
  ans
end
