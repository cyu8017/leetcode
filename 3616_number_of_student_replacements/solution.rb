# LeetCode 3616 - Number of Student Replacements
# https://leetcode.com/problems/number-of-student-replacements/

# @param {Integer[]} ranks
# @return {Integer}
def total_replacements(ranks)
  ans = 0
  cur = ranks[0]
  ranks.each do |x|
    if x < cur
      cur = x
      ans += 1
    end
  end
  ans
end
