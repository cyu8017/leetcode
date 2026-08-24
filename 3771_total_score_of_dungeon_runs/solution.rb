# LeetCode 3771 - Total Score of Dungeon Runs
# https://leetcode.com/problems/total-score-of-dungeon-runs/

# @param {Integer} hp
# @param {Integer[]} damage
# @param {Integer[]} requirement
# @return {Integer}
def total_score(hp, damage, requirement)
  n = damage.length
  prefix = Array.new(n + 1, 0)
  (0...n).each { |i| prefix[i + 1] = prefix[i] + damage[i] }
  answer = n * (n + 1) / 2
  (1..n).each do |j|
    threshold = prefix[j] + (requirement[j - 1] - hp)
    lo = 0
    hi = j
    while lo < hi
      mid = (lo + hi) >> 1
      if prefix[mid] < threshold
        lo = mid + 1
      else
        hi = mid
      end
    end
    answer -= lo
  end
  answer
end
