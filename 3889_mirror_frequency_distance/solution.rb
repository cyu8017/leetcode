# LeetCode 3889 - Mirror Frequency Distance
# https://leetcode.com/problems/mirror-frequency-distance/

# @param {String} s
# @return {Integer}
def mirror_frequency(s)
  freq = Hash.new(0)
  s.each_char { |c| freq[c] += 1 }
  ans = 0
  vis = {}
  freq.each do |c, v|
    m = if c >= "a" && c <= "z"
          (97 + 25 - (c.ord - 97)).chr
        else
          (48 + (9 - (c.ord - 48))).chr
        end
    next if vis[m] == true
    vis[c] = true
    ans += (v - freq[m]).abs
  end
  ans
end
