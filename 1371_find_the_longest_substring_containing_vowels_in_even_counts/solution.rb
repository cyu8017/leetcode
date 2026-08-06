# LeetCode 1371 - Find The Longest Substring Containing Vowels In Even Counts
# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

def find_the_longest_substring(s)
  first = { 0 => -1 }
  mask = 0
  ans = 0
  s.each_char.with_index do |c, i|
    idx = 'aeiou'.index(c)
    mask ^= (1 << idx) if idx
    if first.key?(mask)
      ans = [ans, i - first[mask]].max
    else
      first[mask] = i
    end
  end
  ans
end
