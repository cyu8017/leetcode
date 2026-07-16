# LeetCode 0368 - Largest Divisible Subset
# https://leetcode.com/problems/largest-divisible-subset/

class Solution
  def largest_divisible_subset(nums)
    nums.sort!
    chains = nums.to_h { |num| [num, [num]] }
    best = []

    nums.each do |num|
      chains.each do |prev, chain|
        if prev < num && num % prev == 0 && chain.length + 1 > chains[num].length
          chains[num] = chain + [num]
        end
      end
      best = chains[num] if chains[num].length > best.length
    end

    best
  end

  alias_method :largestDivisibleSubset, :largest_divisible_subset
end
