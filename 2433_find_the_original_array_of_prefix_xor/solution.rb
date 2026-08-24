# LeetCode 2433 - Find The Original Array of Prefix Xor
# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

# @param {Integer[]} pref
# @return {Integer[]}
def find_array(pref)
  ans = Array.new(pref.length, 0)
  ans[0] = pref[0]
  (1...pref.length).each { |i| ans[i] = pref[i] ^ pref[i - 1] }
  ans
end
