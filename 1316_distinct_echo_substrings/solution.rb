# LeetCode 1316 - Distinct Echo Substrings
# https://leetcode.com/problems/distinct-echo-substrings/

def distinct_echo_substrings(text)
  n = text.length
  mod1 = 1_000_000_007
  mod2 = 1_000_000_009
  base = 911382323
  h1 = Array.new(n + 1, 0)
  h2 = Array.new(n + 1, 0)
  p1 = Array.new(n + 1, 1)
  p2 = Array.new(n + 1, 1)
  text.chars.each_with_index do |ch, i|
    code = ch.ord
    h1[i + 1] = (h1[i] * base + code) % mod1
    h2[i + 1] = (h2[i] * base + code) % mod2
    p1[i + 1] = p1[i] * base % mod1
    p2[i + 1] = p2[i] * base % mod2
  end
  hashed = lambda do |left, right|
    length = right - left
    [((h1[right] - h1[left] * p1[length]) % mod1),
     ((h2[right] - h2[left] * p2[length]) % mod2)]
  end
  echoes = {}
  (1..(n / 2)).each do |half|
    (0..(n - 2 * half)).each do |left|
      if hashed.call(left, left + half) == hashed.call(left + half, left + 2 * half)
        echoes[[2 * half] + hashed.call(left, left + 2 * half)] = true
      end
    end
  end
  echoes.length
end
