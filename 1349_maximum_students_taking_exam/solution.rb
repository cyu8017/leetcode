# LeetCode 1349 - Maximum Students Taking Exam
# https://leetcode.com/problems/maximum-students-taking-exam/

def max_students(seats)
  rows = seats.length
  cols = seats[0].length
  valid_rows = seats.map do |row|
    available = 0
    row.each_with_index { |cell, c| available |= (1 << c) if cell == '.' }
    (0...(1 << cols)).select { |mask| (mask & ~available) == 0 && (mask & (mask << 1)) == 0 }
  end
  dp = { 0 => 0 }
  valid_rows.each do |masks|
    nxt = {}
    masks.each do |mask|
      dp.each do |previous, count|
        if (mask & (previous << 1)) == 0 && (mask & (previous >> 1)) == 0
          nxt[mask] = [nxt.fetch(mask, 0), count + mask.to_s(2).count('1')].max
        end
      end
    end
    dp = nxt
  end
  dp.values.max
end
