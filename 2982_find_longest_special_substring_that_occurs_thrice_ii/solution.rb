# LeetCode 2982 - Find Longest Special Substring That Occurs Thrice II
# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/

# @param {String} s
# @return {Integer}
def maximum_length(s)
  groups = Array.new(26) { [] }
  n = s.length
  i = 0
  while i < n
    j = i
    j += 1 while j < n && s[j] == s[i]
    groups[s[i].ord - 97] << (j - i)
    i = j
  end
  ans = -1
  26.times do |c|
    arr = groups[c]
    next if arr.empty?

    arr.sort!.reverse!
    arr[0].downto(1) do |len|
      cnt = 0
      arr.each { |g| cnt += g - len + 1 if g >= len }
      if cnt >= 3
        ans = len if len > ans
        break
      end
    end
  end
  ans
end
