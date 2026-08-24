# LeetCode 3849 - Maximum Bitwise XOR After Rearrangement
# https://leetcode.com/problems/maximum-bitwise-xor-after-rearrangement/

# @param {String} s
# @param {String} t
# @return {String}
def maximum_xor(s, t)
  cnt = [0, 0]
  t.each_byte { |c| cnt[c - 48] += 1 }
  ans = Array.new(s.length, "")
  s.length.times do |i|
    x = s[i].ord - 48
    if cnt[x ^ 1] > 0
      cnt[x ^ 1] -= 1
      ans[i] = "1"
    else
      cnt[x] -= 1
      ans[i] = "0"
    end
  end
  ans.join
end
