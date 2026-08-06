# LeetCode 1125 - Smallest Sufficient Team
# https://leetcode.com/problems/smallest-sufficient-team/

# @param {String[]} req_skills
# @param {String[][]} people
# @return {Integer[]}
def smallest_sufficient_team(req_skills, people)
  skill_index = {}
  req_skills.each_with_index { |s, i| skill_index[s] = i }
  m = req_skills.length
  n = people.length
  target = (1 << m) - 1
  person_mask = people.map do |skills|
    mask = 0
    skills.each { |s| mask |= 1 << skill_index[s] if skill_index.key?(s) }
    mask
  end
  dp = { 0 => [] }
  person_mask.each_with_index do |pmask, i|
    dp.keys.each do |mask|
      team = dp[mask]
      new_mask = mask | pmask
      next if new_mask == mask
      cand = team + [i]
      if !dp.key?(new_mask) || cand.length < dp[new_mask].length
        dp[new_mask] = cand
      end
    end
  end
  dp[target]
end
