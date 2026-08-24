# LeetCode 3167 - Better Compression of String
# https://leetcode.com/problems/better-compression-of-string/

# @param {String} compressed
# @return {String}
def better_compression(compressed)
  cnt = Array.new(26, 0)
  n = compressed.length
  i = 0
  while i < n
    c = compressed[i]
    j = i + 1
    x = 0
    while j < n
      d = compressed[j]
      break if d < "0" || d > "9"
      x = x * 10 + (d.ord - 48)
      j += 1
    end
    cnt[c.ord - 97] += x
    i = j
  end
  ans = []
  26.times do |c|
    if cnt[c] > 0
      ans << (97 + c).chr
      ans << cnt[c].to_s
    end
  end
  ans.join
end
