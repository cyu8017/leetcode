# LeetCode 1481 - Least Number Of Unique Integers After K Removals
# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

def find_least_num_of_unique_ints(arr, k)
  counts = Hash.new(0)
  arr.each { |x| counts[x] += 1 }
  freqs = counts.values.sort
  removed = 0
  freqs.each do |count|
    break if k < count
    k -= count
    removed += 1
  end
  freqs.length - removed
end
