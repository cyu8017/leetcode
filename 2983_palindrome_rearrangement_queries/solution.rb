# LeetCode 2983 - Palindrome Rearrangement Queries
# https://leetcode.com/problems/palindrome-rearrangement-queries/

# @param {String} s
# @param {Integer[][]} queries
# @return {Boolean[]}
def can_make_palindrome_queries(s, queries)
  n = s.length
  m = n / 2
  t = s[m..-1].reverse
  s = s[0...m]
  pre1 = Array.new(m + 1) { Array.new(26, 0) }
  pre2 = Array.new(m + 1) { Array.new(26, 0) }
  diff = Array.new(m + 1, 0)
  (1..m).each do |i|
    26.times do |k|
      pre1[i][k] = pre1[i - 1][k]
      pre2[i][k] = pre2[i - 1][k]
    end
    pre1[i][s[i - 1].ord - 97] += 1
    pre2[i][t[i - 1].ord - 97] += 1
    diff[i] = diff[i - 1] + (s[i - 1] == t[i - 1] ? 0 : 1)
  end
  ans = []
  queries.each do |q|
    a = q[0]
    b = q[1]
    c = n - 1 - q[3]
    d = n - 1 - q[2]
    ans << if a <= c
             pal_check(pre1, pre2, diff, a, b, c, d)
           else
             pal_check(pre2, pre1, diff, c, d, a, b)
           end
  end
  ans
end

def pal_count_pref(pre, i, j)
  cnt = Array.new(26, 0)
  26.times { |k| cnt[k] = pre[j + 1][k] - pre[i][k] }
  cnt
end

def pal_sub_cnt(cnt1, cnt2)
  cnt = Array.new(26, 0)
  26.times do |i|
    cnt[i] = cnt1[i] - cnt2[i]
    return nil if cnt[i] < 0
  end
  cnt
end

def pal_eq_cnt(a, b)
  26.times { |i| return false if a[i] != b[i] }
  true
end

def pal_check(pre1, pre2, diff, a, b, c, d)
  return false if diff[a] > 0 || diff[diff.length - 1] - diff[[b, d].max + 1] > 0
  return pal_eq_cnt(pal_count_pref(pre1, a, b), pal_count_pref(pre2, a, b)) if d <= b
  if b < c
    return diff[c] - diff[b + 1] == 0 &&
           pal_eq_cnt(pal_count_pref(pre1, a, b), pal_count_pref(pre2, a, b)) &&
           pal_eq_cnt(pal_count_pref(pre1, c, d), pal_count_pref(pre2, c, d))
  end
  cnt1 = pal_sub_cnt(pal_count_pref(pre1, a, b), pal_count_pref(pre2, a, c - 1))
  cnt2 = pal_sub_cnt(pal_count_pref(pre2, c, d), pal_count_pref(pre1, b + 1, d))
  !cnt1.nil? && !cnt2.nil? && pal_eq_cnt(cnt1, cnt2)
end
