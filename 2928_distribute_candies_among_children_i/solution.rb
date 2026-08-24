# LeetCode 2928 - Distribute Candies Among Children I
# https://leetcode.com/problems/distribute-candies-among-children-i/

# @param {Integer} n
# @param {Integer} limit
# @return {Integer}
def distribute_candies(n, limit)
  ans = 0
  (0..limit).each do |i|
    (0..limit).each do |j|
      k = n - i - j
      ans += 1 if k >= 0 && k <= limit
    end
  end
  ans
end
