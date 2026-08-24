# LeetCode 3304 - Find the K-th Character in String Game I
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

# @param {Integer} k
# @return {Character}
def kth_character(k)
  s = "a"
  while s.length < k
    n = s.length
    add = ""
    n.times do |i|
      add << (97 + ((s[i].ord - 97 + 1) % 26)).chr
    end
    s += add
  end
  s[k - 1]
end
