# LeetCode 0458 - Poor Pigs
# https://leetcode.com/problems/poor-pigs/

class Solution
  def poor_pigs(buckets, minutes_to_die, minutes_to_test)
    states = minutes_to_test / minutes_to_die + 1
    pigs = 0
    capacity = 1

    while capacity < buckets
      pigs += 1
      capacity *= states
    end

    pigs
  end

  alias_method :poorPigs, :poor_pigs
end
