# LeetCode 2676 - Throttle
# https://leetcode.com/problems/throttle/

# @param {Proc} fn
# @param {Integer} t
# @return {Proc}
def throttle(fn, t)
  last = -Float::INFINITY
  pending = nil
  timer = nil
  run = lambda do |*args|
    last = Time.now.to_f * 1000
    fn.call(*args)
  end
  lambda do |*args|
    now = Time.now.to_f * 1000
    remaining = t - (now - last)
    if remaining <= 0
      timer = nil
      run.call(*args)
    else
      pending = args
      if timer.nil?
        timer = Thread.new do
          sleep(remaining / 1000.0)
          timer = nil
          unless pending.nil?
            a = pending
            pending = nil
            run.call(*a)
          end
        end
      end
    end
  end
end

def solve(*args)
  throttle(*args)
end
