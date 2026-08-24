# LeetCode 2107 - Number of Unique Flavors After Sharing K Candies
# https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/

# @param {Integer[]} candies
# @param {Integer} k
# @return {Integer}
def share_candies(candies, k)
  n = candies.length
  freq = Hash.new(0)
  candies.each { |c| freq[c] += 1 }
  return freq.length if k == 0

  k.times do |i|
    c = candies[i]
    freq[c] -= 1
    freq.delete(c) if freq[c] == 0
  end
  ans = freq.length
  (k...n).each do |i|
    freq[candies[i - k]] += 1
    c = candies[i]
    freq[c] -= 1
    freq.delete(c) if freq[c] == 0
    ans = [ans, freq.length].max
  end
  ans
end
