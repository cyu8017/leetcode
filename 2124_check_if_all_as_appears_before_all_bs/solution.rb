# LeetCode 2124 - Check if All A's Appears Before All B's
# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

# @param {String} s
# @return {Boolean}
def check_string(s)
  seen_b = false
  s.each_char do |c|
    if c == "b"
      seen_b = true
    elsif seen_b
      return false
    end
  end
  true
end
