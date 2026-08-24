# LeetCode 3751 - Total Waviness of Numbers in Range I
# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

# @param {Integer} num1
# @param {Integer} num2
# @return {Integer}
def total_waviness(num1, num2)
  f = lambda do |x|
    nums = []
    while x > 0
      nums << x % 10
      x /= 10
    end
    m = nums.length
    return 0 if m < 3
    s = 0
    (1...(m - 1)).each do |i|
      if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) ||
         (nums[i] < nums[i - 1] && nums[i] < nums[i + 1])
        s += 1
      end
    end
    s
  end
  ans = 0
  (num1..num2).each { |x| ans += f.call(x) }
  ans
end
