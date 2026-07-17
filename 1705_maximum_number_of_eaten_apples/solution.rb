# LeetCode 1705 - Maximum Number of Eaten Apples
# https://leetcode.com/problems/maximum-number-of-eaten-apples/

# @param {Integer[]} apples
# @param {Integer[]} days
# @return {Integer}
def eaten_apples(apples, days)
  # Sorted descending by expire day, so the minimum expire is at the end.
  heap = []
  n = apples.length
  day = 0
  eaten = 0
  while day < n || !heap.empty?
    if day < n && apples[day] > 0
      item = [day + days[day], apples[day]]
      pos = heap.bsearch_index { |entry| entry[0] <= item[0] } || heap.length
      heap.insert(pos, item)
    end
    heap.pop while !heap.empty? && heap[-1][0] <= day
    unless heap.empty?
      expire, count = heap.pop
      eaten += 1
      heap << [expire, count - 1] if count > 1
    end
    day += 1
  end
  eaten
end
