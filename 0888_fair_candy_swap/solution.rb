# LeetCode 0888 - Fair Candy Swap
# https://leetcode.com/problems/fair-candy-swap/

# @param {Integer[]} alice_sizes
# @param {Integer[]} bob_sizes
# @return {Integer[]}
def fair_candy_swap(alice_sizes, bob_sizes)
  diff = (alice_sizes.sum - bob_sizes.sum) / 2
  bob = {}
  bob_sizes.each { |b| bob[b] = true }
  alice_sizes.each do |a|
    return [a, a - diff] if bob.key?(a - diff)
  end
  []
end
