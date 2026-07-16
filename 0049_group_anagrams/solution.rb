# LeetCode 0049 - Group Anagrams
# https://leetcode.com/problems/group-anagrams/

# @param {String[]} strs
# @return {String[][]}
def group_anagrams(strs)
  groups = Hash.new { |hash, key| hash[key] = [] }

  strs.each do |word|
    key = word.chars.sort.join
    groups[key] << word
  end

  result = groups.values.map(&:sort)
  result.sort_by { |group| -group.map { |word| strs.index(word) }.min }
end
