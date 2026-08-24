# LeetCode 2981 - Find Longest Special Substring That Occurs Thrice I
# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

# @param {String} s
# @return {Integer}
def maximum_length(s)
  n = s.length
  ans = -1
  n.times do |i|
    i.upto(n - 1) do |j|
      break if s[j] != s[i]

      length = j - i + 1
      cnt = 0
      (0..n - length).each do |k|
        ok = true
        length.times do |t|
          if s[k + t] != s[i + t]
            ok = false
            break
          end
        end
        cnt += 1 if ok
      end
      ans = length if cnt >= 3 && length > ans
    end
  end
  ans
end
