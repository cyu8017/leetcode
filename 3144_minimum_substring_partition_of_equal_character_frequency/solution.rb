# LeetCode 3144 - Minimum Substring Partition of Equal Character Frequency
# https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/

# @param {String} s
# @return {Integer}
def minimum_substrings_in_partition(s)
  n = s.length
  memo = Array.new(n, -1)

  dfs = lambda do |i|
    return 0 if i >= n
    return memo[i] if memo[i] != -1
    cnt = Array.new(26, 0)
    freq = {}
    memo[i] = n - i
    (i...n).each do |j|
      k = s[j].ord - 97
      if cnt[k] > 0
        c = cnt[k]
        nv = freq[c] - 1
        if nv == 0
          freq.delete(c)
        else
          freq[c] = nv
        end
      end
      cnt[k] += 1
      freq[cnt[k]] = freq.fetch(cnt[k], 0) + 1
      memo[i] = [memo[i], 1 + dfs.call(j + 1)].min if freq.length == 1
    end
    memo[i]
  end

  dfs.call(0)
end
