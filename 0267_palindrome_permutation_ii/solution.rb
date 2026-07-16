# LeetCode 0267 - Palindrome Permutation II
# https://leetcode.com/problems/palindrome-permutation-ii/

# @param {String} s
# @return {String[]}
def generate_palindromes(s)
  counts = Hash.new(0)
  s.each_char { |char| counts[char] += 1 }

  odd_chars = counts.select { |_, count| count.odd? }.keys
  return [] if odd_chars.length > 1

  middle = odd_chars.length == 1 ? odd_chars[0] : ''
  half = []
  counts.keys.sort.each do |char|
    (counts[char] / 2).times { half << char }
  end

  result = []
  used = Array.new(half.length, false)
  path = []

  backtrack = lambda do
    if path.length == half.length
      prefix = path.join
      result << prefix + middle + prefix.reverse
      return
    end
    half.each_with_index do |char, index|
      next if used[index]
      next if index.positive? && half[index] == half[index - 1] && !used[index - 1]

      used[index] = true
      path << char
      backtrack.call
      path.pop
      used[index] = false
    end
  end

  backtrack.call
  result
end
