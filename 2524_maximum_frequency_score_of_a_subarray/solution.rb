# LeetCode 2524 - Maximum Frequency Score of a Subarray
# https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_frequency_score(nums, k)
  mod = 1_000_000_007
  freq = Hash.new(0)

  mod_pow = lambda do |a, e|
    res = 1
    a %= mod
    while e > 0
      res = res * a % mod if e.odd?
      a = a * a % mod
      e >>= 1
    end
    res
  end

  add = lambda do |score, x|
    c = freq[x]
    score = (score - mod_pow.call(x, c) + mod) % mod if c > 0
    freq[x] = c + 1
    (score + mod_pow.call(x, c + 1)) % mod
  end

  remove = lambda do |score, x|
    c = freq[x]
    score = (score - mod_pow.call(x, c) + mod) % mod
    if c == 1
      freq.delete(x)
    else
      freq[x] = c - 1
      score = (score + mod_pow.call(x, c - 1)) % mod
    end
    score
  end

  score = 0
  best = 0
  nums.each_with_index do |num, i|
    score = add.call(score, num)
    score = remove.call(score, nums[i - k]) if i >= k
    best = score if i >= k - 1 && score > best
  end
  best
end

alias solve max_frequency_score
