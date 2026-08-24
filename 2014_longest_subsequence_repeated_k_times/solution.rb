# LeetCode 2014 - Longest Subsequence Repeated k Times
# https://leetcode.com/problems/longest-subsequence-repeated-k-times/

# @param {String} s
# @param {Integer} k
# @return {String}
def longest_subsequence_repeated_k(s, k)
  freq = Array.new(26, 0)
  s.each_char { |c| freq[c.ord - 97] += 1 }
  chars = (25).downto(0).filter_map { |c| (97 + c).chr if freq[c] >= k }.join

  is_subseq = lambda do |t|
    need = 0
    times = 0
    s.each_char do |ch|
      next unless ch == t[need]

      need += 1
      if need == t.length
        times += 1
        return true if times == k

        need = 0
      end
    end
    false
  end

  best = ""
  q = [""]
  until q.empty?
    cur = q.shift
    chars.each_char do |ch|
      nxt = cur + ch
      next unless is_subseq.call(nxt)

      best = nxt if nxt.length > best.length || (nxt.length == best.length && nxt > best)
      q << nxt
    end
  end
  best
end
