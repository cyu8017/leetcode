# LeetCode 1057 - Campus Bikes
# https://leetcode.com/problems/campus-bikes/

# @param {Integer[][]} workers
# @param {Integer[][]} bikes
# @return {Integer[]}
def assign_bikes(workers, bikes)
  triples = []
  workers.each_with_index do |(wx, wy), w|
    bikes.each_with_index do |(bx, by), b|
      triples << [(wx - bx).abs + (wy - by).abs, w, b]
    end
  end
  triples.sort!
  ans = Array.new(workers.length, -1)
  used_bikes = {}
  assigned = 0
  triples.each do |_, w, b|
    next unless ans[w] == -1 && !used_bikes[b]

    ans[w] = b
    used_bikes[b] = true
    assigned += 1
    break if assigned == workers.length
  end
  ans
end
