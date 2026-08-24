# LeetCode 2076 - Process Restricted Friend Requests
# https://leetcode.com/problems/process-restricted-friend-requests/

# @param {Integer} n
# @param {Integer[][]} restrictions
# @param {Integer[][]} requests
# @return {Boolean[]}
def friend_requests(n, restrictions, requests)
  parent = (0...n).to_a
  find = lambda do |x|
    parent[x] = find.call(parent[x]) if parent[x] != x
    parent[x]
  end
  unite = lambda do |a, b|
    a = find.call(a)
    b = find.call(b)
    parent[a] = b if a != b
  end
  ans = Array.new(requests.length, false)
  requests.each_with_index do |(ru, rv), i|
    u = find.call(ru)
    v = find.call(rv)
    ok = true
    if u != v
      restrictions.each do |x0, y0|
        x = find.call(x0)
        y = find.call(y0)
        if (x == u && y == v) || (x == v && y == u)
          ok = false
          break
        end
      end
    end
    ans[i] = ok
    unite.call(u, v) if ok
  end
  ans
end
