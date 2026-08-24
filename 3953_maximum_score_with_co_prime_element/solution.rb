# LeetCode 3953 - Maximum Score with Co-Prime Element
# https://leetcode.com/problems/maximum-score-with-co-prime-element/

# @param {Integer[]} nums
# @param {Integer} max_val
# @return {Integer}
def max_score(nums, max_val)
  bad_count = lambda do |x, divisible|
    primes = []
    y = x
    p = 2
    while p * p <= y
      if y % p == 0
        primes << p
        y /= p while y % p == 0
      end
      p += 1
    end
    primes << y if y > 1
    bad = 0
    psz = primes.length
    (1...(1 << psz)).each do |mask|
      product = 1
      bits = 0
      psz.times do |i|
        if ((mask >> i) & 1) != 0
          product *= primes[i]
          bits += 1
        end
      end
      if bits.odd?
        bad += divisible[product]
      else
        bad -= divisible[product]
      end
    end
    bad
  end
  evaluate = lambda do |x, exists, checked, divisible|
    return -2_147_483_648 / 4 if checked[x]
    checked[x] = true
    bad = bad_count.call(x, divisible)
    cost = if exists
             x > 1 ? bad - 1 : 0
           else
             bad > 0 ? bad : 1
           end
    x - cost
  end
  limit = max_val
  frequency = Array.new(100001, 0)
  nums.each do |x|
    frequency[x] += 1
    limit = x if x > limit
  end
  divisible = Array.new(limit + 1, 0)
  (1..limit).each do |d|
    multiple = d
    while multiple <= limit
      divisible[d] += frequency[multiple] if multiple < frequency.length
      multiple += d
    end
  end
  best = -nums.length
  checked = Array.new(limit + 1, false)
  (1..max_val).each do |x|
    v = evaluate.call(x, x < frequency.length && frequency[x] > 0, checked, divisible)
    best = v if v > best
  end
  nums.each do |x|
    v = evaluate.call(x, true, checked, divisible)
    best = v if v > best
  end
  best
end
