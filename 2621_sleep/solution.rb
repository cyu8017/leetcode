# LeetCode 2621 - Sleep
# https://leetcode.com/problems/sleep/

# @param {Integer} millis
# @return {NilClass}
def sleep(millis)
  Kernel.sleep(millis / 1000.0)
  nil
end

def solve(*args)
  sleep(*args)
end
