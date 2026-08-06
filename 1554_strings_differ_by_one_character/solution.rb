# LeetCode 1554 - Strings Differ by One Character
# https://leetcode.com/problems/strings-differ-by-one-character/

# @param {String[]} dict
# @return {Boolean}
def differ_by_one(dict)
  seen = {}
  dict.each do |word|
    word.length.times do |i|
      pattern = word[0...i] + '*' + word[(i + 1)..]
      return true if seen[pattern]
      seen[pattern] = true
    end
  end
  false
end
