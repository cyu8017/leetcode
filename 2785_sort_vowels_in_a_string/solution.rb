# LeetCode 2785 - Sort Vowels in a String
# https://leetcode.com/problems/sort-vowels-in-a-string/

# @param {String} s
# @return {String}
def sort_vowels(s)
  vowels_set = "aeiouAEIOU"
  vowels = s.chars.select { |c| vowels_set.include?(c) }.sort
  arr = s.chars
  vi = 0
  arr.each_with_index do |c, i|
    if vowels_set.include?(c)
      arr[i] = vowels[vi]
      vi += 1
    end
  end
  arr.join
end
