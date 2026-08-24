# LeetCode 2443 - Sum of Number and Its Reverse
# https://leetcode.com/problems/sum-of-number-and-its-reverse/

# @param {Integer} num
# @return {Boolean}
def sum_of_number_and_reverse(num)
  rev = lambda do |x|
    r = 0
    while x > 0
      r = r * 10 + x % 10
      x /= 10
    end
    r
  end

  (0..num).each { |i| return true if i + rev.call(i) == num }
  false
end
