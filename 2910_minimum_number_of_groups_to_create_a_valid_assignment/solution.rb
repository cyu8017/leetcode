# LeetCode 2910 - Minimum Number of Groups to Create a Valid Assignment
# https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/

# @param {Integer[]} balls
# @return {Integer}
def min_groups_for_valid_assignment(balls)
  freq = {}
  balls.each { |b| freq[b] = freq.fetch(b, 0) + 1 }
  counts = freq.values
  min_f = counts.min
  min_f.downto(1) do |size|
    ok = true
    groups = 0
    counts.each do |c|
      rem = c % (size + 1)
      g2 = c / (size + 1)
      if rem == 0
        groups += g2
      elsif size - rem <= g2
        groups += g2 + 1
      else
        ok = false
        break
      end
    end
    return groups if ok
  end
  balls.length
end
