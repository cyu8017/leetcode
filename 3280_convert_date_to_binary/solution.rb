# LeetCode 3280 - Convert Date to Binary
# https://leetcode.com/problems/convert-date-to-binary/

# @param {String} date
# @return {String}
def convert_date_to_binary(date)
  to_binary = lambda do |v|
    return "0" if v == 0
    s = ""
    while v > 0
      s = (v & 1).to_s + s
      v >>= 1
    end
    s
  end
  y, m, d = date.split("-").map(&:to_i)
  "#{to_binary.call(y)}-#{to_binary.call(m)}-#{to_binary.call(d)}"
end
