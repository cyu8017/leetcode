# LeetCode 1542 - Find Longest Awesome Substring
# https://leetcode.com/problems/find-longest-awesome-substring/

# @param {String} s
# @return {Integer}
def longest_awesome(s)
  first = { 0 => -1 }
  mask = answer = 0
  s.each_char.with_index do |ch, i|
    mask ^= 1 << ch.to_i
    if first.key?(mask)
      answer = [answer, i - first[mask]].max
    else
      first[mask] = i
    end
    10.times do |bit|
      candidate = mask ^ (1 << bit)
      answer = [answer, i - first[candidate]].max if first.key?(candidate)
    end
  end
  answer
end
