
# @param {Integer[]} nums
# @return {Integer}
def count_different_subsequence_g_c_ds(nums)
  max_val = nums.max
  present = Array.new(max_val + 1, false)
  nums.each { |num| present[num] = true }

  ans = 0
  (1..max_val).each do |g|
    has = false
    gcd_val = 0
    (g..max_val).step(g) do |multiple|
      next unless present[multiple]
      has = true
      gcd_val = gcd_val.gcd(multiple / g)
      break if gcd_val == 1
    end
    ans += 1 if has && gcd_val == 1
  end
  ans
end
