# LeetCode 2967 - Minimum Cost to Make Array Equalindromic
# https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/

# @param {Integer[]} nums
# @return {Integer}
def minimum_cost(nums)
  nums.sort!
  n = nums.length
  median = nums[n / 2]
  candidates = [make_pal(median)]
  s = median.to_s
  half = s[0, (s.length + 1) / 2].to_i
  (-2..2).each do |d|
    h = half + d
    next if h <= 0

    hs = h.to_s
    pal = if s.length.even?
            hs + hs.reverse
          else
            hs + hs[0...-1].reverse
          end
    candidates << pal.to_i
  end
  [1, 9, 11, 99, 101].each { |v| candidates << v }
  ans = 1 << 60
  candidates.each do |p|
    next if p <= 0

    c = cost_of(nums, p)
    ans = c if c < ans
  end
  ans
end

def make_pal(x)
  ch = x.to_s.chars
  i = 0
  j = ch.length - 1
  while i < j
    ch[j] = ch[i]
    i += 1
    j -= 1
  end
  ch.join.to_i
end

def cost_of(nums, p)
  c = 0
  nums.each { |v| c += (v - p).abs }
  c
end
