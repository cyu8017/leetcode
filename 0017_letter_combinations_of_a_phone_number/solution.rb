# LeetCode 0017 - Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# @param {String} digits
# @return {String[]}
def letter_combinations(digits)
  return [] if digits.empty?

  mapping = {
    "2" => "abc",
    "3" => "def",
    "4" => "ghi",
    "5" => "jkl",
    "6" => "mno",
    "7" => "pqrs",
    "8" => "tuv",
    "9" => "wxyz",
  }
  result = []

  backtrack = lambda do |index, path|
    if index == digits.length
      result << path.join
      return
    end
    mapping[digits[index]].each_char do |ch|
      backtrack.call(index + 1, path + ch)
    end
  end

  backtrack.call(0, "")
  result
end
