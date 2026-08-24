# LeetCode 2138 - Divide a String Into Groups of Size k
# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

# @param {String} s
# @param {Integer} k
# @param {String} fill
# @return {String[]}
def divide_string(s, k, fill)
  ans = []
  0.step(s.length - 1, k) do |i|
    if i + k <= s.length
      ans << s[i, k]
    else
      chunk = s[i..]
      chunk += fill while chunk.length < k
      ans << chunk
    end
  end
  ans
end
