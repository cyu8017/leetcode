# LeetCode 0982 - Triples with Bitwise AND Equal To Zero
# https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/

# @param {Integer[]} nums
# @return {Integer}
def count_triplets(nums)
  cnt = Hash.new(0)
  nums.each do |a|
    nums.each { |b| cnt[a & b] += 1 }
  end
  ans = 0
  nums.each do |c|
    cnt.each { |ab, times| ans += times if (ab & c).zero? }
  end
  ans
end
