# LeetCode 3692 - Majority Frequency Characters
# https://leetcode.com/problems/majority-frequency-characters/

# @param {String} s
# @return {String}
def majority_frequency_group(s)
  cnt = Array.new(26, 0)
  s.each_char { |c| cnt[c.ord - 97] += 1 }
  f = {}
  (0...26).each do |i|
    f[cnt[i]] = (f[cnt[i]] || "") + (97 + i).chr if cnt[i] > 0
  end
  mx = 0
  mv = 0
  ans = ""
  f.each do |v, cs|
    if cs.length > mx || (cs.length == mx && v > mv)
      mx = cs.length
      mv = v
      ans = cs
    end
  end
  ans
end
