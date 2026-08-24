# LeetCode 2459 - Sort Array By Moving Items to Empty Space
# https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/

# @param {Integer[]} nums
# @return {Integer}
def sort_array(nums)
  solve_one = lambda do |start_zero|
    n = nums.length
    arr = nums.dup
    pos = {}
    arr.each_with_index { |v, i| pos[v] = i }
    ops = 0
    loop do
      empty = pos[0]
      should = start_zero ? empty : (empty == n - 1 ? 0 : empty + 1)
      if arr[empty] == should
        found = -1
        (0...n).each do |i|
          want = start_zero ? i : (i == n - 1 ? 0 : i + 1)
          if arr[i] != want
            found = i
            break
          end
        end
        return ops if found == -1

        v = arr[found]
        arr[empty] = arr[found]
        arr[found] = 0
        pos[0] = found
        pos[v] = empty
        ops += 1
        next
      end
      j = pos[should]
      vv = arr[j]
      arr[empty] = arr[j]
      arr[j] = 0
      pos[0] = j
      pos[vv] = empty
      ops += 1
    end
  end

  [solve_one.call(true), solve_one.call(false)].min
end
