# LeetCode 1673 - Find the Most Competitive Subsequence
# https://leetcode.com/problems/find-the-most-competitive-subsequence/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def most_competitive(nums, k)
  st = []
  nums.each_with_index do |x, i|
    while !st.empty? && st[-1] > x && st.length - 1 + nums.length - i >= k
      st.pop
    end
    st << x if st.length < k
  end
  st
end
