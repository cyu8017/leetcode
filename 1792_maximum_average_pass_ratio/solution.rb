# LeetCode 1792 - Maximum Average Pass Ratio
# https://leetcode.com/problems/maximum-average-pass-ratio/

# @param {Integer[][]} classes
# @param {Integer} extra_students
# @return {Float}
def max_average_ratio(classes, extra_students)
  gain = ->(p, t) { (p + 1).fdiv(t + 1) - p.fdiv(t) }

  heap = classes.map { |p, t| [gain.call(p, t), p, t] }

  sift_down = lambda do |i|
    n = heap.length
    loop do
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
      largest = l if l < n && heap[l][0] > heap[largest][0]
      largest = r if r < n && heap[r][0] > heap[largest][0]
      break if largest == i
      heap[i], heap[largest] = heap[largest], heap[i]
      i = largest
    end
  end

  (heap.length / 2 - 1).downto(0) { |i| sift_down.call(i) }

  extra_students.times do
    _, p, t = heap[0]
    heap[0] = [gain.call(p + 1, t + 1), p + 1, t + 1]
    sift_down.call(0)
  end

  heap.sum { |_, p, t| p.fdiv(t) } / heap.length
end
