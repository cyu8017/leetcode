# LeetCode 2694 - Event Emitter
# https://leetcode.com/problems/event-emitter/

class EventEmitter
  def initialize
    @handlers = {}
  end

  def subscribe(event_name, callback)
    @handlers[event_name] ||= []
    lst = @handlers[event_name]
    lst << callback
    {
      "unsubscribe" => lambda {
        lst.delete(callback)
        nil
      }
    }
  end

  def emit(event_name, args = [])
    args = [] if args.nil?
    lst = @handlers[event_name] || []
    lst.map { |cb| cb.call(*args) }
  end
end

# @param {Object} actions
# @param {Object} values
# @return {EventEmitter}
def event_emitter(_actions = nil, _values = nil)
  EventEmitter.new
end

def solve(*args)
  event_emitter(*args)
end
