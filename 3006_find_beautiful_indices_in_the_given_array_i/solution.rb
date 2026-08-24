# LeetCode 3006 - Find Beautiful Indices in the Given Array I
# https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/

# @param {String} s
# @param {String} a
# @param {String} b
# @param {Integer} k
# @return {Integer[]}
def beautiful_indices(s, a, b, k)
  lps_a = Array.new(a.length, 0)
  lps_b = Array.new(b.length, 0)
  a_index = []
  b_index = []
  result = []
  build_lps(lps_a, a)
  build_lps(lps_b, b)
  kmp_collect(s, a, lps_a, a_index)
  kmp_collect(s, b, lps_b, b_index)
  i = 0
  j = 0
  while i < a_index.length && j < b_index.length
    if a_index[i] + k >= b_index[j] && a_index[i] - k <= b_index[j]
      result << a_index[i]
      i += 1
    elsif a_index[i] - k > b_index[j]
      j += 1
    else
      i += 1
    end
  end
  result
end

def build_lps(lps, pattern)
  l = 0
  i = 1
  s_l = pattern.length
  lps[0] = 0
  while i < s_l
    if pattern[i] == pattern[l]
      l += 1
      lps[i] = l
      i += 1
    elsif l != 0
      l = lps[l - 1]
    else
      lps[i] = l
      i += 1
    end
  end
end

def kmp_collect(s, pat, lps, index)
  s_len = s.length
  pat_l = pat.length
  i = 0
  j = 0
  while s_len - i >= pat_l - j
    if s[i] == pat[j]
      i += 1
      j += 1
    end
    if j == pat_l
      index << i - pat_l
      j = lps[j - 1]
    elsif i < s_len && s[i] != pat[j]
      if j != 0
        j = lps[j - 1]
      else
        i += 1
      end
    end
  end
end
