# LeetCode 3137 - Minimum Number of Operations to Make Word K-Periodic
# https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/

# @param {String} word
# @param {Integer} k
# @return {Integer}
def minimum_operations_to_make_k_periodic(word, k)
  cnt = Hash.new(0)
  n = word.length
  mx = 0
  (0...n).step(k) do |i|
    s = word[i, k]
    cnt[s] += 1
    mx = [mx, cnt[s]].max
  end
  n / k - mx
end
