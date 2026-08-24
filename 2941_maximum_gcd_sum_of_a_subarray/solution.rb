# LeetCode 2941 - Maximum GCD-Sum of a Subarray
# https://leetcode.com/problems/maximum-gcd-sum-of-a-subarray/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_gcd_sum(nums, k)
  n = nums.length
  pref = Array.new(n + 1, 0)
  n.times { |i| pref[i + 1] = pref[i] + nums[i] }
  ans = 0
  st = []
  n.times do |i|
    nst = [[nums[i], i]]
    st.each do |p|
      g = nums[i].gcd(p[0])
      if nst[-1][0] == g
        nst[-1][1] = p[1] if p[1] < nst[-1][1]
        next
      end
      nst << [g, p[1]]
    end
    st = nst
    st.each do |g, idx|
      if i - idx + 1 >= k
        cand = (pref[i + 1] - pref[idx]) * g
        ans = cand if cand > ans
      end
    end
  end
  ans
end

def solve(*args)
  max_gcd_sum(*args)
end
