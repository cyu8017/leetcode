# LeetCode 0898 - Bitwise ORs of Subarrays
# https://leetcode.com/problems/bitwise-ors-of-subarrays/

# @param {Integer[]} arr
# @return {Integer}
def subarray_bitwise_o_rs(arr)
  ans = {}
  cur = {}
  arr.each do |x|
    nxt = { x => true }
    cur.each_key { |y| nxt[x | y] = true }
    cur = nxt
    cur.each_key { |v| ans[v] = true }
  end
  ans.length
end
