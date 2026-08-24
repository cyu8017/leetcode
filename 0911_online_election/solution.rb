# LeetCode 0911 - Online Election
# https://leetcode.com/problems/online-election/

class TopVotedCandidate
  def initialize(persons, times)
    counts = Hash.new(0)
    leader = -1
    @events = []
    persons.zip(times).each do |person, time|
      counts[person] += 1
      leader = person if counts[person] >= counts[leader]
      @events << [time, leader]
    end
  end

  def q(t)
    lo = 0
    hi = @events.length
    while lo < hi
      mid = (lo + hi) / 2
      if @events[mid][0] <= t
        lo = mid + 1
      else
        hi = mid
      end
    end
    @events[lo - 1][1]
  end
end
