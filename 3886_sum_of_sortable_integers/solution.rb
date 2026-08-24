# LeetCode 3886 - Sum of Sortable Integers
# https://leetcode.com/problems/sum-of-sortable-integers/

# @param {Integer[]} nums
# @return {Integer}
def sum_of_sortable_integers(nums)
  rotation_matches = lambda do |block, target|
    k = block.length
    prefix = Array.new(k, 0)
    (1...k).each do |i|
      j = prefix[i - 1]
      while j > 0 && target[i] != target[j]
        j = prefix[j - 1]
      end
      j += 1 if target[i] == target[j]
      prefix[i] = j
    end
    matched = 0
    (0...(2 * k - 1)).each do |i|
      x = block[i % k]
      matched = prefix[matched - 1] while matched > 0 && x != target[matched]
      matched += 1 if x == target[matched]
      return true if matched == k
    end
    false
  end
  n = nums.length
  sorted_nums = nums.sort
  divisors = []
  d = 1
  while d * d <= n
    if n % d == 0
      divisors << d
      divisors << n / d if d * d != n
    end
    d += 1
  end
  answer = 0
  divisors.each do |k|
    ok = true
    (0...n).step(k) do |start|
      block = nums[start, k]
      target = sorted_nums[start, k]
      unless rotation_matches.call(block, target)
        ok = false
        break
      end
    end
    answer += k if ok
  end
  answer
end
