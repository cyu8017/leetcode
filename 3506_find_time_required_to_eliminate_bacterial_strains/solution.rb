# LeetCode 3506 - Find Time Required to Eliminate Bacterial Strains
# https://leetcode.com/problems/find-time-required-to-eliminate-bacterial-strains/

# @param {Integer[]} time_req
# @param {Integer} split_time
# @return {Integer}
def min_elimination_time(time_req, split_time)
  pq = time_req.sort
  while pq.length > 1
    pq.shift
    x = pq.shift
    v = x + split_time
    lo = 0
    hi = pq.length
    while lo < hi
      mid = (lo + hi) >> 1
      if pq[mid] < v
        lo = mid + 1
      else
        hi = mid
      end
    end
    pq.insert(lo, v)
  end
  pq[0]
end
