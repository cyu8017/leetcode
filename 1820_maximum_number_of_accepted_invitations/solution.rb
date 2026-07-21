
# @param {Integer[][]} grid
# @return {Integer}
def maximum_invitations(grid)
  boys = grid.length
  girls = grid[0].length
  match_girl = Array.new(girls, -1)

  dfs = lambda do |boy, seen|
    girls.times do |girl|
      next unless grid[boy][girl] == 1 && !seen[girl]
      seen[girl] = true
      if match_girl[girl] == -1 || dfs.call(match_girl[girl], seen)
        match_girl[girl] = boy
        return true
      end
    end
    false
  end

  ans = 0
  boys.times do |boy|
    ans += 1 if dfs.call(boy, Array.new(girls, false))
  end
  ans
end
