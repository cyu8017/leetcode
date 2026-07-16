# LeetCode 0274 - H-Index
# https://leetcode.com/problems/h-index/

# @param {Integer[]} citations
# @return {Integer}
def h_index(citations)
  buckets = Array.new(citations.length + 1, 0)
  citations.each do |citation|
    buckets[[citation, citations.length].min] += 1
  end
  total = 0
  (buckets.length - 1).downto(0) do |h|
    total += buckets[h]
    return h if total >= h
  end
  0
end
