# LeetCode 0784 - Letter Case Permutation
# https://leetcode.com/problems/letter-case-permutation/

# @param {String} s
# @return {String[]}
def letter_case_permutation(s)
  result = [""]
  s.each_char do |ch|
    result = if ch.match?(/[A-Za-z]/)
               result.flat_map { |prefix| [prefix + ch.downcase, prefix + ch.upcase] }
             else
               result.map { |prefix| prefix + ch }
             end
  end
  result
end
