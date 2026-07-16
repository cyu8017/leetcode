# LeetCode 0358 - Rearrange String k Distance Apart
# https://leetcode.com/problems/rearrange-string-k-distance-apart/

class Solution
  def rearrange_string(s, k)
    counts = Hash.new(0)
    s.each_char { |char| counts[char] += 1 }

    max_freq = counts.values.max
    max_freq_chars = counts.values.count(max_freq)
    return "" if (s.length - max_freq_chars) < (max_freq - 1) * (k - 1)

    heap = counts.map { |char, count| [-count, char] }
    heapify = lambda do |items|
      n = items.length
      ((n / 2) - 1).downto(0) do |index|
        bubble_down = lambda do |start|
          smallest = start
          left = 2 * start + 1
          right = left + 1
          smallest = left if left < n && items[left] < items[smallest]
          smallest = right if right < n && items[right] < items[smallest]
          if smallest != start
            items[start], items[smallest] = items[smallest], items[start]
            bubble_down.call(smallest)
          end
        end
        bubble_down.call(index)
      end
    end
    heapify.call(heap)

    heap_push = lambda do |items, item|
      items << item
      index = items.length - 1
      while index > 0
        parent = (index - 1) / 2
        break if items[parent] <= items[index]

        items[parent], items[index] = items[index], items[parent]
        index = parent
      end
    end

    heap_pop = lambda do |items|
      top = items[0]
      last = items.pop
      if items.any?
        items[0] = last
        index = 0
        loop do
          smallest = index
          left = 2 * index + 1
          right = left + 1
          smallest = left if left < items.length && items[left] < items[smallest]
          smallest = right if right < items.length && items[right] < items[smallest]
          break if smallest == index

          items[index], items[smallest] = items[smallest], items[index]
          index = smallest
        end
      end
      top
    end

    queue = []
    result = []
    index = 0

    while heap.any? || queue.any?
      while queue.any? && queue.first[2] <= index
        count, char, = queue.shift
        heap_push.call(heap, [count, char])
      end

      return "" if heap.empty?

      count, char = heap_pop.call(heap)
      result << char
      queue << [count + 1, char, index + k] if count + 1 < 0
      index += 1
    end

    result.join
  end

  alias_method :rearrangeString, :rearrange_string
end
