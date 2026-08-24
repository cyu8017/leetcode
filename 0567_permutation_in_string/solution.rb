# LeetCode 0567 - Permutation in String
# https://leetcode.com/problems/permutation-in-string/

# @param {String} s1
# @param {String} s2
# @return {Boolean}
def check_inclusion(s1, s2)
  need = s1.length
  return false if need > s2.length

  target = Hash.new(0)
  s1.each_char { |ch| target[ch] += 1 }
  window = Hash.new(0)
  left = 0

  s2.each_char.with_index do |char, right|
    window[char] += 1
    while right - left + 1 > need
      window[s2[left]] -= 1
      window.delete(s2[left]) if window[s2[left]].zero?
      left += 1
    end
    return true if window == target
  end

  false
end
