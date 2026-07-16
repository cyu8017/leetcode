# LeetCode 0320 - Generalized Abbreviation
# https://leetcode.com/problems/generalized-abbreviation/

class Solution
  def generateAbbreviations(word)
    result = []
    backtrack = lambda do |index, path, count|
      if index == word.length
        result << path + (count == 0 ? '' : count.to_s)
        return
      end
      backtrack.call(index + 1, path, count + 1)
      next_path = path + (count == 0 ? '' : count.to_s) + word[index]
      backtrack.call(index + 1, next_path, 0)
    end
    backtrack.call(0, '', 0)
    result
  end
end
