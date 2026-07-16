# LeetCode 0275 - H-Index II
# https://leetcode.com/problems/h-index-ii/

# @param {Integer[]} citations
# @return {Integer}
def h_index(citations)
  left = 0
  right = citations.length - 1
  length = citations.length
  while left <= right
    mid = (left + right) / 2
    papers = length - mid
    if citations[mid] >= papers
      right = mid - 1
    else
      left = mid + 1
    end
  end
  length - left
end
