# LeetCode 0781 - Rabbits in Forest
# https://leetcode.com/problems/rabbits-in-forest/

# @param {Integer[]} answers
# @return {Integer}
def num_rabbits(answers)
  total = 0
  answers.tally.each do |answer, count|
    group = answer + 1
    groups = (count + group - 1) / group
    total += groups * group
  end
  total
end
