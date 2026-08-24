# LeetCode 3309 - Maximum Possible Number by Binary Concatenation
# https://leetcode.com/problems/maximum-possible-number-by-binary-concatenation/

# @param {Integer} x
# @return {String}
def to_bin_str(x)
  return "0" if x == 0

  s = ""
  while x > 0
    s = (x & 1).to_s + s
    x >>= 1
  end
  s
end

# @param {Integer} i
# @param {Integer[]} idx
# @param {String[]} bs
# @param {Integer[]} ans
# @return {void}
def perm_bin_concat(i, idx, bs, ans)
  if i == 3
    s = bs[idx[0]] + bs[idx[1]] + bs[idx[2]]
    v = 0
    s.each_char { |c| v = v * 2 + (c.ord - 48) }
    ans[0] = v if v > ans[0]
    return
  end
  (i...3).each do |j|
    idx[i], idx[j] = idx[j], idx[i]
    perm_bin_concat(i + 1, idx, bs, ans)
    idx[i], idx[j] = idx[j], idx[i]
  end
end

# @param {Integer[]} nums
# @return {Integer}
def max_good_number(nums)
  bs = [to_bin_str(nums[0]), to_bin_str(nums[1]), to_bin_str(nums[2])]
  idx = [0, 1, 2]
  ans = [0]
  perm_bin_concat(0, idx, bs, ans)
  ans[0]
end
