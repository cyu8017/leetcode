# LeetCode 0710 - Random Pick with Blacklist
# https://leetcode.com/problems/random-pick-with-blacklist/

$uniform = ->(_a, _b) { rand }

def set_uniform(uniform_fn)
  $uniform = uniform_fn
end

class Solution
  def initialize(n, blacklist)
    @size = n - blacklist.length
    black = {}
    blacklist.each { |b| black[b] = true }
    whites = (@size...n).select { |x| !black[x] }
    wi = 0
    @mapping = {}
    blacklist.each do |b|
      next unless b < @size

      @mapping[b] = whites[wi]
      wi += 1
    end
  end

  def pick
    index = $uniform.call(0, @size).to_i
    index = @size - 1 if index >= @size
    @mapping.fetch(index, index)
  end
end
