# LeetCode 0564 - Find the Closest Palindrome
# https://leetcode.com/problems/find-the-closest-palindrome/

# @param {String} n
# @return {String}
def nearest_palindromic(n)
  length = n.length
  number = n.to_i
  candidates = [
    10**(length - 1) - 1,
    10**length + 1
  ]

  prefix = n[0, (length + 1) / 2].to_i
  [prefix - 1, prefix, prefix + 1].each do |half|
    text = half.to_s
    palindrome = if length.even?
                   text + text.reverse
                 else
                   text + text[0...-1].reverse
                 end
    candidates << palindrome.to_i
  end

  candidates.uniq!
  candidates.delete(number)
  candidates.min_by { |value| [((value - number).abs), value] }.to_s
end
