# LeetCode 1456 - Maximum Number Of Vowels In A Substring Of Given Length
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

def max_vowels(s, k)
  vowels = { 'a' => true, 'e' => true, 'i' => true, 'o' => true, 'u' => true }
  cur = s[0, k].chars.count { |c| vowels[c] }
  ans = cur
  (k...s.length).each do |i|
    cur += (vowels[s[i]] ? 1 : 0) - (vowels[s[i - k]] ? 1 : 0)
    ans = [ans, cur].max
  end
  ans
end
