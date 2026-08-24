# LeetCode 2491 - Divide Players Into Teams of Equal Skill
# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

# @param {Integer[]} skill
# @return {Integer}
def divide_players(skill)
  skill = skill.sort
  n = skill.length
  target = skill[0] + skill[n - 1]
  chem = 0
  (n / 2).times do |i|
    return -1 if skill[i] + skill[n - 1 - i] != target

    chem += skill[i] * skill[n - 1 - i]
  end
  chem
end
