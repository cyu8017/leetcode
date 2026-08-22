# LeetCode 3991 - Sort Array Using Prefix Reversals
# https://leetcode.com/problems/sort-array-using-prefix-reversals/

# @param {Integer[]} nums
# @param {Integer[]} pre
# @return {Integer}
def sort_array(nums, pre)
  n = nums.length
  start = nums.join(",")
  target = (0...n).to_a.join(",")
  return 0 if start == target

  lengths = pre.select { |i| i >= 2 && i <= n }.uniq.sort
  visited = { start => true }
  queue = [nums.dup]
  steps = 0

  until queue.empty?
    steps += 1
    next_queue = []
    queue.each do |cur|
      lengths.each do |i|
        nxt = cur.dup
        l = 0
        r = i - 1
        while l < r
          nxt[l], nxt[r] = nxt[r], nxt[l]
          l += 1
          r -= 1
        end
        key = nxt.join(",")
        return steps if key == target
        unless visited[key]
          visited[key] = true
          next_queue << nxt
        end
      end
    end
    queue = next_queue
  end
  -1
end
