# LeetCode 2748 - Number of Beautiful Pairs
# https://leetcode.com/problems/number-of-beautiful-pairs/

# @param {Integer[]} nums
# @return {Integer}
def count_beautiful_pairs(nums)
  def gcd(a, b)
    while b != 0
      a, b = b, a % b
    end
    a
  end

  firsts = nums.map { |x| x.to_s[0].ord - 48 }
  lasts = nums.map { |x| x % 10 }
  ans = 0
  (0...nums.length).each do |i|
    ((i + 1)...nums.length).each do |j|
      ans += 1 if gcd(firsts[i], lasts[j]) == 1
    end
  end
  ans
end
