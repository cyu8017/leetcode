# LeetCode 0749 - Contain Virus
# https://leetcode.com/problems/contain-virus/

# @param {Integer[][]} is_infected
# @return {Integer}
def contain_virus(is_infected)
  m = is_infected.length
  n = is_infected[0].length
  walls = 0

  neighbors = lambda do |r, c|
    [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]].select do |nr, nc|
      nr >= 0 && nr < m && nc >= 0 && nc < n
    end
  end

  loop do
    seen = {}
    regions = []
    frontiers = []
    perimeters = []

    m.times do |i|
      n.times do |j|
        next unless is_infected[i][j] == 1 && !seen[[i, j]]

        stack = [[i, j]]
        seen[[i, j]] = true
        region = {}
        frontier = {}
        perimeter = 0
        until stack.empty?
          r, c = stack.pop
          region[[r, c]] = true
          neighbors.call(r, c).each do |nr, nc|
            if is_infected[nr][nc] == 1 && !seen[[nr, nc]]
              seen[[nr, nc]] = true
              stack << [nr, nc]
            elsif is_infected[nr][nc] == 0
              frontier[[nr, nc]] = true
              perimeter += 1
            end
          end
        end
        regions << region
        frontiers << frontier
        perimeters << perimeter
      end
    end

    break if regions.empty?

    quarantine = (0...regions.length).max_by { |idx| frontiers[idx].length }
    break if frontiers[quarantine].empty?

    walls += perimeters[quarantine]
    regions[quarantine].each_key { |r, c| is_infected[r][c] = -1 }

    frontiers.each_with_index do |frontier, index|
      next if index == quarantine

      frontier.each_key { |r, c| is_infected[r][c] = 1 }
    end
  end

  walls
end
