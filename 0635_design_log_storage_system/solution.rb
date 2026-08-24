# LeetCode 0635 - Design Log Storage System
# https://leetcode.com/problems/design-log-storage-system/

class LogSystem
  def initialize
    @logs = []
    @granularity_index = {
      "Year" => 4,
      "Month" => 7,
      "Day" => 10,
      "Hour" => 13,
      "Minute" => 16,
      "Second" => 19
    }
  end

  def put(id, timestamp)
    @logs << [id, timestamp]
    nil
  end

  def retrieve(start_time, end_time, granularity)
    index = @granularity_index[granularity]
    start_key = start_time[0, index]
    end_key = end_time[0, index]
    matched = @logs.filter_map do |log_id, timestamp|
      key = timestamp[0, index]
      [timestamp, log_id] if start_key <= key && key <= end_key
    end
    matched.sort.map { |_, log_id| log_id }
  end
end
