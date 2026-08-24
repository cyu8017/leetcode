# LeetCode 3885 - Design Event Manager
# https://leetcode.com/problems/design-event-manager/

class EventManager
  def initialize(events)
    @sl = []
    @d = {}
    events.each do |e|
      event_id, priority = e[0], e[1]
      @sl << [-priority, event_id]
      @d[event_id] = priority
    end
    _sort
  end

  def update_priority(event_id, new_priority)
    old = @d[event_id]
    @sl.reject! { |x| x[0] == -old && x[1] == event_id }
    @sl << [-new_priority, event_id]
    @d[event_id] = new_priority
    _sort
    nil
  end

  def poll_highest
    return -1 if @sl.empty?
    top = @sl.shift
    event_id = top[1]
    @d.delete(event_id)
    event_id
  end

  def _sort
    @sl.sort_by! { |a| [a[0], a[1]] }
  end
end
