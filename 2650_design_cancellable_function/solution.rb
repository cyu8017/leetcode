# LeetCode 2650 - Design Cancellable Function
# https://leetcode.com/problems/design-cancellable-function/

# @param {Enumerator} generator
# @return {Array}
def cancellable(generator)
  cancelled = false
  cancel = lambda { cancelled = true }
  run = lambda do
    enum = generator
    nxt = enum.next
    loop do
      begin
        value = nxt.respond_to?(:call) ? nxt.call : nxt
        nxt = if cancelled
                enum.raise(RuntimeError, "Cancelled")
              else
                enum.feed(value)
                enum.next
              end
      rescue StopIteration => e
        return e.result
      rescue StandardError => e
        begin
          nxt = enum.raise(e)
        rescue StopIteration => se
          return se.result
        end
      end
    end
  end
  [cancel, run]
end
