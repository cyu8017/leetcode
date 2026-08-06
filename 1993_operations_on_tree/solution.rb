# LeetCode 1993 - Operations on Tree
# https://leetcode.com/problems/operations-on-tree/

class LockingTree
  # @param {Integer[]} parent
  def initialize(parent)
    n = parent.length
    @locked = Array.new(n, -1)
    @parent = parent
    @children = Array.new(n) { [] }
    (1...n).each { |son| @children[parent[son]] << son }
  end

  # @param {Integer} num
  # @param {Integer} user
  # @return {Boolean}
  def lock(num, user)
    return false unless @locked[num] == -1
    @locked[num] = user
    true
  end

  # @param {Integer} num
  # @param {Integer} user
  # @return {Boolean}
  def unlock(num, user)
    return false unless @locked[num] == user
    @locked[num] = -1
    true
  end

  # @param {Integer} num
  # @param {Integer} user
  # @return {Boolean}
  def upgrade(num, user)
    x = num
    while x != -1
      return false unless @locked[x] == -1
      x = @parent[x]
    end

    found = [false]
    dfs = lambda do |u|
      @children[u].each do |v|
        if @locked[v] != -1
          @locked[v] = -1
          found[0] = true
        end
        dfs.call(v)
      end
    end
    dfs.call(num)
    return false unless found[0]
    @locked[num] = user
    true
  end
end
