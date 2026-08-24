# LeetCode 0850 - Rectangle Area II
# https://leetcode.com/problems/rectangle-area-ii/

# @param {Integer[][]} rectangles
# @return {Integer}
def rectangle_area(rectangles)
  mod = 10**9 + 7
  events = []
  rectangles.each do |x1, y1, x2, y2|
    events << [x1, 1, y1, y2]
    events << [x2, -1, y1, y2]
  end
  events.sort!

  covered_length = lambda do |active|
    return 0 if active.empty?

    active = active.sort
    total = 0
    cur_start, cur_end = active[0]
    active[1..].each do |start, finish|
      if start > cur_end
        total += cur_end - cur_start
        cur_start = start
        cur_end = finish
      else
        cur_end = [cur_end, finish].max
      end
    end
    total + cur_end - cur_start
  end

  active = []
  area = 0
  prev_x = events[0][0]
  events.each do |x, typ, y1, y2|
    area += covered_length.call(active) * (x - prev_x)
    if typ == 1
      active << [y1, y2]
    else
      idx = active.index([y1, y2])
      active.delete_at(idx)
    end
    prev_x = x
  end
  area % mod
end
