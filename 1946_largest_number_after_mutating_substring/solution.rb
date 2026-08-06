# LeetCode 1946 - Largest Number After Mutating Substring
# https://leetcode.com/problems/largest-number-after-mutating-substring/

# @param {String} num
# @param {Integer[]} change
# @return {String}
def maximum_number(num, change)
  chars = num.chars
  started = false
  chars.each_with_index do |ch, i|
    d = ch.to_i
    mapped = change[d]
    if mapped > d
      chars[i] = mapped.to_s
      started = true
    elsif mapped < d && started
      break
    end
  end
  chars.join
end
