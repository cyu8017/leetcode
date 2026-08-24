# LeetCode 0943 - Find the Shortest Superstring
# https://leetcode.com/problems/find-the-shortest-superstring/

# @param {String[]} words
# @return {String}
def shortest_superstring(words)
  n = words.length
  overlap = Array.new(n) { Array.new(n, 0) }
  n.times do |i|
    n.times do |j|
      next if i == j

      a = words[i]
      b = words[j]
      [a.length, b.length].min.downto(1) do |k|
        if a.end_with?(b[0, k])
          overlap[i][j] = k
          break
        end
      end
    end
  end

  dp = Array.new(1 << n) { Array.new(n, "") }
  n.times { |i| dp[1 << i][i] = words[i] }

  (1 << n).times do |mask|
    n.times do |last|
      next if (mask & (1 << last)).zero? || dp[mask][last].empty?

      n.times do |nxt|
        next unless (mask & (1 << nxt)).zero?

        cand = dp[mask][last] + words[nxt][overlap[last][nxt]..]
        nmask = mask | (1 << nxt)
        if dp[nmask][nxt].empty? || cand.length < dp[nmask][nxt].length
          dp[nmask][nxt] = cand
        end
      end
    end
  end

  full = (1 << n) - 1
  candidates = dp[full].reject(&:empty?)
  candidates << words.join
  best_len = candidates.map(&:length).min
  candidates.select { |s| s.length == best_len }.min
end
