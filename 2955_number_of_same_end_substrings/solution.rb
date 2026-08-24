# LeetCode 2955 - Number of Same-End Substrings
# https://leetcode.com/problems/number-of-same-end-substrings/

# @param {String} s
# @param {Integer[][]} queries
# @return {Integer[]}
def same_end_substring_count(s, queries)
  n = s.length
  pref = Array.new(n + 1) { Array.new(26, 0) }
  n.times do |i|
    26.times { |c| pref[i + 1][c] = pref[i][c] }
    pref[i + 1][s[i].ord - 97] += 1
  end
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |(l, r), qi|
    total = 0
    26.times do |c|
      cnt = pref[r + 1][c] - pref[l][c]
      total += cnt * (cnt + 1) / 2
    end
    ans[qi] = total
  end
  ans
end

def solve(*args)
  same_end_substring_count(*args)
end
