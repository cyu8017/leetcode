# LeetCode 2601 - Prime Subtraction Operation
# https://leetcode.com/problems/prime-subtraction-operation/

# @param {Integer[]} nums
# @return {Boolean}
def prime_sub_operation(nums)
  max_v = 0
  nums.each { |x| max_v = x if x > max_v }
  is_p = Array.new(max_v + 1, true)
  is_p[0] = false if max_v >= 0
  is_p[1] = false if max_v >= 1
  i = 2
  while i * i <= max_v
    if is_p[i]
      j = i * i
      while j <= max_v
        is_p[j] = false
        j += i
      end
    end
    i += 1
  end
  primes = (2..max_v).select { |x| is_p[x] }
  prev = 0
  nums.each do |x|
    need = x - prev
    best = -1
    primes.each do |p|
      break if p >= need

      best = p
    end
    cur = best < 0 ? x : x - best
    return false if cur <= prev

    prev = cur
  end
  true
end
