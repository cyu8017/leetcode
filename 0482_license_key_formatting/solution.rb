# LeetCode 0482 - License Key Formatting
# https://leetcode.com/problems/license-key-formatting/

class Solution
  def license_key_formatting(s, k)
    chars = s.each_char.reject { |ch| ch == "-" }.map(&:upcase)
    return "" if chars.empty?

    first_len = chars.length % k
    first_len = k if first_len == 0
    parts = [chars[0, first_len].join]
    index = first_len
    while index < chars.length
      parts << chars[index, k].join
      index += k
    end
    parts.join("-")
  end

  alias_method :licenseKeyFormatting, :license_key_formatting
end
