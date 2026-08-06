# LeetCode 1271 - Hexspeak
# https://leetcode.com/problems/hexspeak/

# @param {String} num
# @return {String}
def to_hexspeak(num)
  value = num.to_i
  digits = "0123456789ABCDEF"
  out = ""
  while value > 0
    value, rem = value.divmod(16)
    return "ERROR" if rem.between?(2, 9)
    out = digits[rem] + out
  end
  (out.empty? ? "0" : out).tr("01", "OI")
end
