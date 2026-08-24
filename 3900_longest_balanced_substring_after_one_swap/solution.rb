# LeetCode 3900 - Longest Balanced Substring After One Swap
# https://leetcode.com/problems/longest-balanced-substring-after-one-swap/

# @param {String} s
# @return {Integer}
def longest_balanced(s)
  cnt0 = s.count("0")
  cnt1 = s.length - cnt0
  pos = {}
  pos[0] = [-1]
  ans = 0
  pre = 0
  s.length.times do |i|
    pre += s[i] == "1" ? 1 : -1
    pos[pre] ||= []
    pos[pre] << i
    ans = [ans, i - pos[pre][0]].max
    if pos.key?(pre - 2)
      p = pos[pre - 2]
      if (i - p[0] - 2) / 2 < cnt0
        ans = [ans, i - p[0]].max
      elsif p.length > 1
        ans = [ans, i - p[1]].max
      end
    end
    if pos.key?(pre + 2)
      p = pos[pre + 2]
      if (i - p[0] - 2) / 2 < cnt1
        ans = [ans, i - p[0]].max
      elsif p.length > 1
        ans = [ans, i - p[1]].max
      end
    end
  end
  ans
end
