# LeetCode 3577 - Count the Number of Computer Unlocking Permutations
# https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/

# @param {Integer[]} complexity
# @return {Integer}
def count_permutations(complexity)
  mod = 1000000007
  ans = 1
  (1...complexity.length).each do |i|
    return 0 if complexity[i] <= complexity[0]
    ans = ans * i % mod
  end
  ans
end
