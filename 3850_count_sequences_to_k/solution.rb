# LeetCode 3850 - Count Sequences to K
# https://leetcode.com/problems/count-sequences-to-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def count_sequences(nums, k)
  f = {}
  gcd = lambda do |a, b|
    while b != 0
      a, b = b, a % b
    end
    a
  end
  dfs = nil
  dfs = lambda do |i, p, q|
    return (p == k && q == 1) ? 1 : 0 if i == nums.length
    key = "#{i},#{p},#{q}"
    return f[key] if f.key?(key)
    res = dfs.call(i + 1, p, q)
    x = nums[i]
    g1 = gcd.call(p * x, q)
    res += dfs.call(i + 1, (p * x) / g1, q / g1)
    g2 = gcd.call(p, q * x)
    res += dfs.call(i + 1, p / g2, (q * x) / g2)
    f[key] = res
    res
  end
  dfs.call(0, 1, 1)
end
