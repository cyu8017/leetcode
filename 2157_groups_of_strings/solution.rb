# LeetCode 2157 - Groups of Strings
# https://leetcode.com/problems/groups-of-strings/

# @param {String[]} words
# @return {Integer[]}
def group_strings(words)
  parent = {}
  size = {}
  find = nil
  find = lambda do |x|
    parent[x] = find.call(parent[x]) if parent[x] != x
    parent[x]
  end
  unite = lambda do |a, b|
    ra = find.call(a)
    rb = find.call(b)
    return if ra == rb

    ra, rb = rb, ra if size[ra] < size[rb]
    parent[rb] = ra
    size[ra] += size[rb]
  end
  mask_of = lambda do |w|
    m = 0
    w.each_byte { |b| m |= 1 << (b - 97) }
    m
  end

  freq = Hash.new(0)
  words.each { |w| freq[mask_of.call(w)] += 1 }
  freq.each do |k, v|
    parent[k] = k
    size[k] = v
  end
  freq.each_key do |m|
    26.times do |b|
      if (m & (1 << b)) != 0
        nm = m ^ (1 << b)
        unite.call(m, nm) if freq.key?(nm)
        26.times do |a|
          if (nm & (1 << a)).zero?
            rm = nm | (1 << a)
            unite.call(m, rm) if freq.key?(rm)
          end
        end
      else
        nm = m | (1 << b)
        unite.call(m, nm) if freq.key?(nm)
      end
    end
  end
  groups = 0
  max_size = 0
  seen = {}
  freq.each_key do |m|
    r = find.call(m)
    next if seen[r]

    seen[r] = true
    groups += 1
    max_size = [max_size, size[r]].max
  end
  [groups, max_size]
end
