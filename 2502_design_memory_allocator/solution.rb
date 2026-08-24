# LeetCode 2502 - Design Memory Allocator
# https://leetcode.com/problems/design-memory-allocator/

class Allocator
  def initialize(n)
    @mem = Array.new(n, 0)
  end

  def allocate(size, m_id)
    free_cnt = 0
    @mem.each_index do |i|
      if @mem[i] == 0
        free_cnt += 1
        if free_cnt == size
          start = i - size + 1
          (start..i).each { |j| @mem[j] = m_id }
          return start
        end
      else
        free_cnt = 0
      end
    end
    -1
  end

  def free_memory(m_id)
    cnt = 0
    @mem.each_index do |i|
      if @mem[i] == m_id
        @mem[i] = 0
        cnt += 1
      end
    end
    cnt
  end
end
