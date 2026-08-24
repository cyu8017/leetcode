# LeetCode 3628 - Maximum Number of Subsequences After One Inserting
# https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/

# @param {String} s
# @return {Integer}
def num_of_subsequences(s)
  calc = lambda do |st, t|
    cnt = 0
    a = 0
    st.each_char do |c|
      cnt += a if c == t[1]
      a += 1 if c == t[0]
    end
    cnt
  end
  l = 0
  r = 0
  s.each_char { |c| r += 1 if c == "T" }
  ans = 0
  mx = 0
  s.each_char do |c|
    r -= 1 if c == "T"
    ans += l * r if c == "C"
    l += 1 if c == "L"
    mx = l * r if l * r > mx
  end
  mx = [mx, calc.call(s, "LC"), calc.call(s, "CT")].max
  ans + mx
end
