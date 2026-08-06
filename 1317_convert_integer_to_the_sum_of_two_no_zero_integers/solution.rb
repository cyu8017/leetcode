# LeetCode 1317 - Convert Integer To The Sum Of Two No Zero Integers
# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

def get_no_zero_integers(n)
  (1...n).each do |first|
    return [first, n - first] if !first.to_s.include?('0') && !(n - first).to_s.include?('0')
  end
  []
end
