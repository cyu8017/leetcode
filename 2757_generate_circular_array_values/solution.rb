# LeetCode 2757 - Generate Circular Array Values
# https://leetcode.com/problems/generate-circular-array-values/

# @param {Object[]} arr
# @param {Integer} start_index
# @return {Enumerator}
def cycle_generator(arr, start_index)
  Enumerator.new do |y|
    i = start_index
    jump = y.yield(arr[i])
    loop do
      n = arr.length
      jump = 0 if jump.nil?
      i = ((i + jump) % n + n) % n
      jump = y.yield(arr[i])
    end
  end
end
