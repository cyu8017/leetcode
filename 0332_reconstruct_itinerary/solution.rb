# LeetCode 0332 - Reconstruct Itinerary
# https://leetcode.com/problems/reconstruct-itinerary/

class Solution
  def find_itinerary(tickets)
    targets = Hash.new { |hash, key| hash[key] = [] }
    tickets.sort.reverse_each do |source, destination|
      targets[source] << destination
    end

    route = []

    visit = lambda do |airport|
      while targets[airport].any?
        visit.call(targets[airport].pop)
      end
      route << airport
    end

    visit.call("JFK")
    route.reverse
  end

  alias_method :findItinerary, :find_itinerary
end
