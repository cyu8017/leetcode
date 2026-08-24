# LeetCode 3491 - Phone Number Prefix
# https://leetcode.com/problems/phone-number-prefix/

# @param {String[]} numbers
# @return {Boolean}
def phone_prefix(numbers)
  numbers = numbers.sort
  (0...(numbers.length - 1)).each do |i|
    return false if numbers[i].length <= numbers[i + 1].length && numbers[i + 1].start_with?(numbers[i])
  end
  true
end
