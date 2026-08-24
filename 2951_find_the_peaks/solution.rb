# LeetCode 2951 - Find the Peaks
# https://leetcode.com/problems/find-the-peaks/

# @param {Integer[]} mountain
# @return {Integer[]}
def find_peaks(mountain)
  ans = []
  (1...mountain.length - 1).each do |i|
    ans << i if mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1]
  end
  ans
end
