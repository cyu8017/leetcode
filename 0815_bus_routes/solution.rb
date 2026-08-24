# LeetCode 0815 - Bus Routes
# https://leetcode.com/problems/bus-routes/

# @param {Integer[][]} routes
# @param {Integer} source
# @param {Integer} target
# @return {Integer}
def num_buses_to_destination(routes, source, target)
  return 0 if source == target

  stop_to_buses = Hash.new { |h, k| h[k] = [] }
  routes.each_with_index do |stops, bus|
    stops.each { |stop| stop_to_buses[stop] << bus }
  end

  queue = [[source, 0]]
  seen_stops = { source => true }
  seen_buses = {}
  until queue.empty?
    stop, buses_taken = queue.shift
    stop_to_buses[stop].each do |bus|
      next if seen_buses[bus]

      seen_buses[bus] = true
      routes[bus].each do |nxt|
        return buses_taken + 1 if nxt == target
        next if seen_stops[nxt]

        seen_stops[nxt] = true
        queue << [nxt, buses_taken + 1]
      end
    end
  end
  -1
end
