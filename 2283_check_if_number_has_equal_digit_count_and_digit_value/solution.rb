# LeetCode 2283 - Check if Number Has Equal Digit Count and Digit Value
# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

# @param {String} num
# @return {Boolean}
def digit_count(num)
  cnt = Array.new(10, 0)
  num.each_char { |c| cnt[c.ord - 48] += 1 }
  num.length.times { |i| return false if cnt[i] != num[i].ord - 48 }
  true
end
