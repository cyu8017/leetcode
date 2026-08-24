# LeetCode 2889 - Reshape Data: Pivot
# https://leetcode.com/problems/reshape-data-pivot/

# @param {Object[]} weather
# @return {Object[]}
def pivot_table(weather)
  months = []
  by_month = {}
  weather.each do |r|
    if r.is_a?(Array)
      city, month, temperature = r[0], r[1], r[2]
    else
      city, month, temperature = r["city"], r["month"], r["temperature"]
    end
    unless by_month.key?(month)
      by_month[month] = {}
      months << month
    end
    by_month[month][city] = temperature
  end
  months.map { |month| { "month" => month }.merge(by_month[month]) }
end
