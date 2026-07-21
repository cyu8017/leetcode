
MOD = 10**9 + 7

# @param {Integer[]} nums
# @return {Integer}
def count_nice_pairs(nums)
  freq = Hash.new(0)
  ans = 0
  nums.each do |num|
    diff = num - rev_num(num)
    ans = (ans + freq[diff]) % MOD
    freq[diff] += 1
  end
  ans
end

def rev_num(x)
  x.to_s.reverse.to_i
end
