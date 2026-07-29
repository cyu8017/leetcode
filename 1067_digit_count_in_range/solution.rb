# LeetCode 1067 - Digit Count in Range
# https://leetcode.com/problems/digit-count-in-range/

# @param {Integer} d
# @param {Integer} low
# @param {Integer} high
# @return {Integer}
def digits_count(d, low, high)
  count_upto = lambda do |n|
    return 0 if n < 0

    s = n.to_s
    length = s.length
    ans = 0
    length.times do |i|
      left = i.positive? ? s[0...i].to_i : 0
      right = i + 1 < length ? s[(i + 1)..].to_i : 0
      digit = s[i].to_i
      power = 10**(length - i - 1)
      if d != 0
        ans += left * power
        if digit > d
          ans += power
        elsif digit == d
          ans += right + 1
        end
      else
        next if i.zero?

        ans += (left - 1) * power
        if digit.positive?
          ans += power
        else
          ans += right + 1
        end
      end
    end
    ans
  end

  count_upto.call(high) - count_upto.call(low - 1)
end
