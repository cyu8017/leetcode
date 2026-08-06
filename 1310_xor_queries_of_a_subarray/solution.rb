# LeetCode 1310 - Xor Queries Of A Subarray
# https://leetcode.com/problems/xor-queries-of-a-subarray/

def xor_queries(arr, queries)
  prefix = [0]
  arr.each { |value| prefix << (prefix[-1] ^ value) }
  queries.map { |left, right| prefix[right + 1] ^ prefix[left] }
end
