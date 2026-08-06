# LeetCode 1996 - The Number of Weak Characters in the Game
# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

# @param {Integer[][]} properties
# @return {Integer}
def number_of_weak_characters(properties)
  properties = properties.sort_by { |x| [x[0], -x[1]] }
  ans = 0
  max_def = 0
  (properties.length - 1).downto(0) do |i|
    if properties[i][1] < max_def
      ans += 1
    else
      max_def = properties[i][1]
    end
  end
  ans
end
