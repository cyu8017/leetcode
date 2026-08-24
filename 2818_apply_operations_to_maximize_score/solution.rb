# LeetCode 2818 - Apply Operations to Maximize Score
# https://leetcode.com/problems/apply-operations-to-maximize-score/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximum_score(nums, k)
  mod = 1_000_000_007
  n = nums.length
  max_v = nums.max || 0
  spf = Array.new(max_v + 1, 0)
  (2..max_v).each do |i|
    next unless spf[i] == 0
    i.step(max_v, i) { |j| spf[j] = i if spf[j] == 0 }
  end
  prime_score = lambda do |x|
    seen = {}
    while x > 1
      p = spf[x]
      seen[p] = true
      x /= p while x % p == 0
    end
    seen.length
  end
  score = nums.map { |v| prime_score.call(v) }
  left = Array.new(n, 0)
  right = Array.new(n, 0)
  st = []
  (0...n).each do |i|
    st.pop while !st.empty? && score[st[-1]] < score[i]
    left[i] = st.empty? ? -1 : st[-1]
    st << i
  end
  st.clear
  (n - 1).downto(0) do |i|
    st.pop while !st.empty? && score[st[-1]] <= score[i]
    right[i] = st.empty? ? n : st[-1]
    st << i
  end
  arr = (0...n).map { |i| [nums[i], (i - left[i]) * (right[i] - i)] }
  arr.sort_by! { |p| -p[0] }
  mod_pow = lambda do |a, b|
    res = 1
    base = a % mod
    exp = b
    while exp > 0
      res = res * base % mod if exp.odd?
      base = base * base % mod
      exp >>= 1
    end
    res
  end
  ans = 1
  remain = k
  arr.each do |val, cnt|
    break if remain <= 0
    use = cnt < remain ? cnt : remain
    ans = ans * mod_pow.call(val, use) % mod
    remain -= use
  end
  ans
end
