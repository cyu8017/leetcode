# LeetCode 1860 - Incremental Memory Leak
# https://leetcode.com/problems/incremental-memory-leak/

# @param {Integer} memory1
# @param {Integer} memory2
# @return {Integer[]}
def mem_leak(memory1, memory2)
  second = 1
  while memory1 >= second || memory2 >= second
    if memory1 >= memory2
      memory1 -= second
    else
      memory2 -= second
    end
    second += 1
  end
  [second, memory1, memory2]
end
