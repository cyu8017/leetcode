# LeetCode 1396 - Design Underground System
# https://leetcode.com/problems/design-underground-system/

class UndergroundSystem
  def initialize
    @ins = {}
    @stats = {}
  end

  def check_in(id, station_name, t)
    @ins[id] = [station_name, t]
  end

  def check_out(id, station_name, t)
    start, begin_t = @ins.delete(id)
    total, count = @stats.fetch([start, station_name], [0, 0])
    @stats[[start, station_name]] = [total + t - begin_t, count + 1]
  end

  def get_average_time(start_station, end_station)
    total, count = @stats[[start_station, end_station]]
    total.to_f / count
  end
end
